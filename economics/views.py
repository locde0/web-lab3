from django.shortcuts import render, get_object_or_404
from .models import MainPage, Program, Department, ExchangeProgram
from datetime import date

def home(request):
    main_page = MainPage.objects.first()
    return render(request, 'economics/home.html', {'main_page': main_page})

def programs(request):
    all_programs = Program.objects.all()
    return render(request, 'economics/programs.html', {'programs': all_programs})

def program_detail(request, pk):
    program = get_object_or_404(Program, pk=pk)
    return render(request, 'economics/program_detail.html', {'program': program})

def departments(request):
    all_departments = Department.objects.all()
    return render(request, 'economics/departments.html', {'departments': all_departments})

def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'economics/department_detail.html', {'department': department})

def exchange_programs(request):
    exchange_list = ExchangeProgram.objects.all()
    today = date.today()
    return render(request, 'economics/exchange.html', {
        'exchange_list': exchange_list,
        'today': today
    })
