from django.shortcuts import render, redirect
from .forms  import CreateUserForm,LoginForm,RecordForm,UpdateRecordForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from .models import Record



def homepage(request):
    return render(request, 'webapp/index.html')

#-- register a user
def register(request):
    
    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    
    context = {'form' :form}
    return render(request, 'webapp/register.html', context=context)


#--login our user
def login_page(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)


        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')


            user = authenticate(request, username = username , password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")
    context = {'login_form':form}

    return render(request, 'webapp/my_login.html', context=context)

#-- dashboard 
@login_required(login_url='login')
def dashboard(request):

    record = Record.objects.all()

    context = {'record' : record }
    return render(request, 'webapp/dashboard.html', context=context)
    

#-- create a record
login_required(login_url='login') 
def  add_record(request):
    
    form = RecordForm()
    
    if request.method == "POST":
        form = RecordForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("dashboard")
        
    context = {'create_record' : form}
    return render(request,'webapp/create-record.html', context = context)




@login_required(login_url='login')
def update_record(request,pk):
    record = Record.objects.get(id=pk)
    form =UpdateRecordForm(instance=record)

    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()
            return redirect("dashboard")
        
    context = {'update_record_form' : form}

    return render(request, 'webapp/update-record.html', context=context)



login_required(login_url='login')
def view_record(request,pk):

    all_record = Record.objects.get(id=pk)

    context = {'record' : all_record}

    return render(request, 'webapp/view-record.html', context=context)


login_required(login_url='login')
def delete_record(request,pk):
    record = Record.objects.get(id=pk)

    record.delete()
    return redirect("dashboard")



# logout
def user_logout(request):
    auth.logout(request)

    return redirect("login")


