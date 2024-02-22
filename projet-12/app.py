from PySide6 import QtWidgets
import currency_converter

class App(QtWidgets.QWidget):
    """Contains all methods to build the application."""

    def __init__(self):
        super().__init__()
        self.c = currency_converter.CurrencyConverter()
        self.setWindowTitle('Convertisseur de devises')
        self.setup_ui()
        self.setup_connections()
        self.set_default_values()
        self.setup_css()


    def setup_ui(self):
        """Create the user interface."""
        self.layout = QtWidgets.QHBoxLayout(self)

        self.cbb_currencies_from = QtWidgets.QComboBox()
        self.spn_amount = QtWidgets.QSpinBox()
        self.btn_reverse = QtWidgets.QPushButton('⇄')
        self.cbb_currencies_to = QtWidgets.QComboBox()
        self.spn_converted_amount = QtWidgets.QSpinBox()

        self.layout.addWidget(self.cbb_currencies_from)
        self.layout.addWidget(self.spn_amount)
        self.layout.addWidget(self.btn_reverse)
        self.layout.addWidget(self.cbb_currencies_to)
        self.layout.addWidget(self.spn_converted_amount)


    def set_default_values(self):
        """Initialize values for app widgets"""
        self.cbb_currencies_from.addItems(sorted(list(self.c.currencies)))
        self.cbb_currencies_to.addItems(sorted(list(self.c.currencies)))
        self.cbb_currencies_from.setCurrentText('EUR')
        self.cbb_currencies_to.setCurrentText('USD')

        self.spn_amount.setRange(1, 1000000000)
        self.spn_converted_amount.setRange(1, 1000000000)
        self.spn_amount.setValue(100)


    def setup_connections(self):
        """Create connections between widgets and methods"""
        self.cbb_currencies_from.activated.connect(self.compute)
        self.cbb_currencies_to.activated.connect(self.compute)
        self.spn_amount.valueChanged.connect(self.compute)
        self.btn_reverse.clicked.connect(self.reverse_currencies)


    def setup_css(self):
        """Set app interface style"""
        self.setStyleSheet('''
        background-color: rgb(30, 30, 30);
        color: rgb(240, 240, 240);
        border: none;
        ''')


    def compute(self):
        """Calculate the converted amount with selected currencies and amount"""
        amount = self.spn_amount.value()
        currency_from = self.cbb_currencies_from.currentText()
        currency_to = self.cbb_currencies_to.currentText()

        try:
            result = self.c.convert(amount, currency_from, currency_to)
        except currency_converter.currency_converter.RateNotFoundError:
            print('La conversion a échoué')
        else:
            self.spn_converted_amount.setValue(result)


    def reverse_currencies(self):
        """Reverse the currencies"""
        currency_from = self.cbb_currencies_from.currentText()
        currency_to = self.cbb_currencies_to.currentText()

        self.cbb_currencies_from.setCurrentText(currency_to)
        self.cbb_currencies_to.setCurrentText(currency_from)

        self.compute()

app = QtWidgets.QApplication([])
win = App()
win.show()
win.resize(450, 50)

app.exec()