from django.shortcuts import render,get_object_or_404, redirect
from .models import StudentModel
# Create your views here.

def list_view(request):
    display = StudentModel.objects.all()
    return render(request,'list_view.html',{'display':display})

def create(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('age') and request.POST.get('phone') and request.POST.get('course'):
            s = StudentModel()
            s.name = request.POST.get('name')
            s.age = request.POST.get('age')
            s.phone = request.POST.get('phone')
            s.course = request.POST.get('course')
            s.save()
            return redirect('list_view')
    return render(request, 'create.html')

#update
def update_info(request, pk):
    update_field = get_object_or_404(StudentModel, pk=pk)

    if request.method == 'POST':           
        if(request.POST.get('new_name') == ''):
            new_name = update_field.name
        else:
            new_name = request.POST.get('new_name')

        if(request.POST.get('new_age') == ''):
            new_age = update_field.age
        else:
            new_age = request.POST.get('new_age')
            
        if(request.POST.get('new_phone') == ''):
            new_phone = update_field.phone
        else:
            new_phone = request.POST.get('new_phone')

        if(request.POST.get('new_course') == ''):
            new_course = update_field.course
        else:
            new_course = request.POST.get('new_course')

        update_field.name = new_name
        update_field.age = new_age
        update_field.phone = new_phone
        update_field.course = new_course

        update_field.save()
        return redirect('list_view')
    return render(request,'update_form.html',{'update_list': update_field})

def delete_info(request, pk):
    info = get_object_or_404(StudentModel, pk=pk)
    info.delete()
    return redirect('list_view')

