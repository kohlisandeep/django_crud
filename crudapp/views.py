from django.shortcuts import render, redirect
from django.views import View
from .models import Student
from .forms import AddStudentForm


# Create your views here.


class Home(View):
    def get(self,request):
        stu_data = Student.objects.all()
        return render(request, 'crudapp/home.html', {'studata' : stu_data})


class Add_Student(View):

    def get(self, request):
        fm = AddStudentForm()
        return render(request ,'crudapp/add-student.html', {'form':fm})

    def post(self,request):
        fm=AddStudentForm(request.POST) # use to take all the input from add form
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'crudapp/add-student.html', {'form': fm})


class Delete_Student(View):
    def post(self,request):
        data = request.POST
        id = data.get('id') # use to take the id of the deleted row
        studata = Student.objects.get(id=id)
        studata.delete()
        return redirect('/')
        # always use try and catch while deleting

class EditStudent(View):
    def get(self, request,id):
        stu = Student.objects.get(id=id)
        fm = AddStudentForm(instance=stu)
        return render(request, 'crudapp/edit-student.html', {'form':fm}) # by this we are providing form to edit

    def post(self,request, id):
        stu = Student.objects.get(id=id) # use to take data we have to update
        fm = AddStudentForm(request.POST, instance=stu) # all data will come under this fm
        if fm.is_valid():
            fm.save()
            return redirect('/')



