from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee,Designation
from .forms import EmployeeCreationForm, DesignationCreationForm, ProfileImageForm
from django.contrib import messages
from BMS.utils import get_decoded_id
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def employee_index(request):
	employees = Employee.objects.all()
	contex = {
		'employees': employees,
		'title': 'Employee' 
	}
	return render(request, 'employee/index.html', contex)

@csrf_exempt
def employee_list(request):
	table_fields = ['name', 'employee_id', 'designation', 'email', 'status']
	if request.method == 'POST':
		start, length = request.POST['start'], request.POST['length']
		order_type = request.POST['order[0][dir]']
		order_column_index = request.POST['order[0][column]']
		
		for p in request.POST:
			print(p)
	
		query_total = Employee.objects.order_by('-'+table_fields[int(order_column_index)]) if order_type == 'desc' else Employee.objects.order_by(table_fields[int(order_column_index)])
		query = query_total[int(start):int(start)+int(length)]
		data = []
		for q in query:
			row = []
			row.append(q.name)
			row.append(q.employee_id)
			row.append(q.designation.title)
			row.append(q.email)
			row.append('<span class="label label-'+('success"' if q.status else 'default"')+'>'+q.get_status()+'</span>')
			# action = '<a href="'+{% url "Employees:employee_detail" q.get_encoded_id() %}+'"><span class="glyphicon glyphicon-search text-success"></span></a>| <a href="{% url "Employees:employee_save"'+ q.get_encoded_id() +' %}?next={{ request.path }}"><span class="glyphicon glyphicon-edit text-info"></span></a>| <a href="{% url "Employees:employee_delete" '+q.get_encoded_id()+ '%}" onclick="return confirm("Are you sure to delete this employee?")"><span class="glyphicon glyphicon-remove text-warning"></span></a>'
			row.append("action")
			data.append(row)

		json_test = json.dumps({'draw': request.POST['draw'], 'recordsTotal': len(query_total), 'recordsFiltered': len(query_total), "data":data})
		return HttpResponse(json_test, content_type = 'application/json')

def employee_detail(request, id):
	employee = get_object_or_404(Employee, pk = get_decoded_id(id))
	if request.method == 'POST':
		old_image = employee.profile_image
		profile_image_form = ProfileImageForm(request.POST or None, request.FILES or None, instance = employee)
		if profile_image_form.is_valid():
			employee = profile_image_form.save()
			if old_image:
				import os
				os.remove(old_image.path)
			messages.success(request, "Profile image has been successfully updated")
			return redirect('Employees:employee_detail', employee.get_encoded_id())
		else:
			messages.success(request, "Problem in uploading image.Try again")

	profile_image_form = ProfileImageForm()
	return render(request, 'employee/detail.html', {'employee': employee, 'profile_image_form': profile_image_form})

def employee_save(request, id = None):
	instance = get_object_or_404(Employee, pk = get_decoded_id(id)) if id else None
	form=EmployeeCreationForm(request.POST or None, instance = instance)
	next = request.GET.get('next')
	if request.method == 'POST':
		if form.is_valid():
			instance=form.save(commit=False)
			if id:
				instance.updated_by = request.user.id
			else:
				instance.created_by = request.user.id
			instance.save()
			messages.success(request, "Employee has been successfully "+ ("updated" if id else "added") +"!")
			return redirect('Employees:employee_detail', instance.get_encoded_id())
	
	contex={
		"form":form,
		'title': 'Update Employee' if id else 'Add Employee',
		'next': next
	}
	return render(request,"employee/save.html",contex)

def employee_delete(request, id):
	employee = get_object_or_404(Employee, pk = get_decoded_id(id))
	employee.delete()
	messages.success(request, "Employee has been successfully deleted!")
	return redirect('Employees:employee_index')

def designation_index(request):
	designations = Designation.objects.all()
	contex = {
		'designations': designations,
		'title': 'Designation'
	}
	return render(request, 'designation/index.html', contex)

def designation_save(request, id = None):
	designation = None if id == None else Designation.objects.get(pk = id)
	form = DesignationCreationForm(request.POST or None, instance = designation)
	if request.method == 'POST':
		if form.is_valid():
			designation = form.save(commit = False)
			if id:
				designation.updated_by = request.user.id
			else:
				designation.created_by = request.user.id
			designation.save()
			messages.success(request, "Designation has been successfully "+ ("created" if id==None else "updated"))
		else:
			messages.error(request, "Designation has not been successfully "+ ("created" if id==None else "updated"))
	contex = {
		'form': form,
		'title': 'Designation'
	}
	return render(request, 'modal_form/save.html', contex)

def designation_delete(request, id):
	designation = get_object_or_404(Designation, pk = get_decoded_id(id))
	designation.delete()
	messages.success(request, "Designation has been successfully deleted")
	return redirect('Employees:designation_index')

