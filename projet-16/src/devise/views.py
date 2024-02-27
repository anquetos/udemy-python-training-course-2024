from django.shortcuts import render, redirect

import api


def redirect_index(request):
    return redirect('home', days_range=30, currencies='EUR')


def dashboard(request, days_range=30, currencies='EUR'):
    days, rates = api.get_rates(currencies=currencies.split(','), n_days=days_range)
    page_label = {7: 'Semaine', 30: 'Mois', 365: 'Année'}.get(days_range, 'Personnalisé')

    return render(request, 'devise/index.html', context={
        'data': rates, 'days_labels': days, 'currencies': currencies, 'page_label': page_label})
