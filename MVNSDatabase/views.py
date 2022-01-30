from django.shortcuts import render, redirect
from .forms import AddDataForm, EditDataForm
from .models import MvnsCollectedData
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'MVNSDatabase/index.html', {'page_title': 'Home'})


def login(request):
    return render(request, 'MVNSDatabase/mvns_login.html', {'page_title': 'Login'})


@login_required
def view(request):
    allData = MvnsCollectedData.objects.all()
    if allData.count() == 0:
        allData = {}
    else:
        allData = allData
    context = {
        'page_title': 'View',
        'allData': allData,
    }
    return render(request, 'MVNSDatabase/mvns_view.html', context)


def search_data(request):
    if 'enteredOrderNumber' in request.POST:
        orNum = request.POST['enteredOrderNumber']
        if orNum == '':
            messages.info(request, f'Please enter something on the search bar')
        else:
            data = MvnsCollectedData.objects.filter(orderNumber=orNum)
            if data.count() == 0:
                messages.warning(request, f'The Order Number "{orNum}" is not found')
            else:
                return redirect('MVNS-found-data', data[0].pk)
    context = {
        'page_title': 'Search Data',
    }
    return render(request, 'MVNSDatabase/mvns_search_data.html', context)


def found_data(request, pk=None):
    dataID = MvnsCollectedData.objects.get(id=pk)
    context = {
        'page_title': 'Edit Data',
        'dataID': dataID,
    }
    return render(request, 'MVNSDatabase/mvns_found_data.html', context)


@login_required()
def add_data(request):
    addForm = AddDataForm()
    if request.method == 'POST':
        addForm = AddDataForm(request.POST)
        if addForm.is_valid():
            addForm.save()
            return redirect('/view')
    context = {
        'page_title': 'Add Data',
        'addForm': addForm,
    }
    return render(request, 'MVNSDatabase/mvns_add_data.html', context)


@login_required()
def edit_data(request, pk=None):
    dataID = MvnsCollectedData.objects.get(id=pk)
    info = EditDataForm(instance=dataID)
    editForm = EditDataForm()
    if request.method == 'POST':
        editForm = EditDataForm(request.POST, instance=dataID)
        if editForm.is_valid():
            editForm.save()
            return redirect('/view')
    context = {
        'page_title': 'Edit Data',
        'info': info,
    }
    return render(request, 'MVNSDatabase/mvns_edit_data.html', context)
