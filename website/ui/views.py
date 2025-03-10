from django.shortcuts import render, redirect
from .models import Personnel, EmploymentDetails, Identification, Position

def dashboard(request):
    return render(request, 'ui/dashboard.html')

def attendance(request):
    return render(request, 'ui/attendance.html')

def add_employee(request):
    if request.method == 'POST':
        # Personnel
        name = request.POST.get('name')
        birthdate = request.POST.get('birthdate')
        birth_place = request.POST.get('birth_place')
        present_address = request.POST.get('present_address')
        provincial_address = request.POST.get('provincial_address')
        contact_number = request.POST.get('contact_number')
        marital_status = request.POST.get('marital_status')
        spouse_name = request.POST.get('spouse_name')

        personnel = Personnel.objects.create(
            name=name,
            birthdate=birthdate,
            birth_place=birth_place,
            present_address=present_address,
            provincial_address=provincial_address,
            contact_number=contact_number,
            marital_status=marital_status,
            spouse_name=spouse_name
        )

        # Employment Details
        position_name = request.POST.get('position')
        position, created = Position.objects.get_or_create(position_name=position_name)
        status = request.POST.get('status')
        date_hired = request.POST.get('date_hired')
        latest_evaluation = request.POST.get('latest_evaluation')
        basic_salary = request.POST.get('basic_salary')

        EmploymentDetails.objects.create(
            personnel=personnel,
            position=position,
            status=status,
            date_hired=date_hired,
            latest_evaluation=latest_evaluation,
            basic_salary=basic_salary
        )

        # Identifications
        sss = request.POST.get('sss')
        philhealth = request.POST.get('philhealth')
        pag_ibig = request.POST.get('pag_ibig')
        tin = request.POST.get('tin')

        Identification.objects.create(
            personnel=personnel,
            sss=sss,
            philhealth=philhealth,
            pag_ibig=pag_ibig,
            tin=tin
        )

    return render(request, 'ui/add_employees.html')

def payroll_computations(request):
    return render(request, 'ui/payroll_computations.html')

def personnel_profile(request):
    return render(request, 'ui/personnel_profile.html')