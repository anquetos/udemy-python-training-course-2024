from PySide6 import QtWidgets, QtCore

from movie import get_movies
from movie import Movie


class App(QtWidgets.QWidget):
    """Contains all methods to build the application."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ciné Club')
        self.setup_ui()
        self.setup_connections()
        self.populate_movies()

    def setup_ui(self):
        """Create the user interface."""
        self.layout = QtWidgets.QVBoxLayout(self)

        self.le_movie_title = QtWidgets.QLineEdit()
        self.btn_add_movie = QtWidgets.QPushButton('Ajouter un film')
        self.lw_movies = QtWidgets.QListWidget()
        self.lw_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_remove_movies = QtWidgets.QPushButton('Supprimer le(s) film(s)')

        self.layout.addWidget(self.le_movie_title)
        self.layout.addWidget(self.btn_add_movie)
        self.layout.addWidget(self.lw_movies)
        self.layout.addWidget(self.btn_remove_movies)

    def setup_connections(self):
        """Create connections between widgets and methods"""
        self.le_movie_title.returnPressed.connect(self.add_movie)
        self.btn_add_movie.clicked.connect(self.add_movie)
        self.btn_remove_movies.clicked.connect(self.remove_movie)

    def populate_movies(self):
        """Populate the list widget with the movies from the DB"""
        movies = get_movies()

        for movie in movies:
            # Create the item to display
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            # Connect an object (the instance of the movie) to the item
            lw_item.setData(QtCore.Qt.UserRole, movie)
            # Add item in the list widget
            self.lw_movies.addItem(lw_item)

    def add_movie(self):
        """Add the movie entered in the text box in the widget and the DB"""
        movie_to_add = self.le_movie_title.text()

        if not movie_to_add:
            return False

        movie = Movie(movie_to_add)
        response = movie.add_to_movies()

        if response:
            # Create the item to display
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            # Connect an object (the instance of the movie) to the item
            lw_item.setData(QtCore.Qt.UserRole, movie)
            # Add item in the list widget
            self.lw_movies.addItem(lw_item)

        self.le_movie_title.setText('')

    def remove_movie(self):
        """Remove selected movie(s) from the widget and the DB"""
        for selected_item in self.lw_movies.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            self.lw_movies.takeItem(self.lw_movies.row(selected_item))


app = QtWidgets.QApplication([])
win = App()
win.show()

app.exec()
