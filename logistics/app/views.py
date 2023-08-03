import random

from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Users
from .models import Message
from .models import Items
from .models import Comment


def user_logout(request):
    logout(request)
    return redirect('index')

def index(request):
    comment = Comment.objects.all().order_by('-id')
    if request.method == ('POST'):
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        emails = Message.objects.create(name=name, email=email, message=message)
        emails.save()
        messages.success(request, 'mail was successfully sent')
        return redirect('index')
    context = {
        'comment': comment,
    }
    return render(request, 'index2.html', context)

def search(request):
    if request.method == 'GET':
        search = request.GET.get('track')

        item = Items.objects.all().filter(booking_mode=search)
    context = {
        'item': item,
    }
    return render(request, 'goods.html', context)

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'welcome back to work', username)
            return redirect('admin_page')
        else:
            messages.info(request, 'username or password is incorrect')
            return redirect('admin_login')
    context = {
        'message': messages,
    }
    return render(request, 'login.html', context)

@login_required(login_url='aadmin_login')
def admin_page(request):
    users = Users.objects.all()
    users = Users.objects.filter(is_superuser=False)
    emails = Message.objects.all()
    item = Items.objects.all()
    comment = Comment.objects.all()
    context = {
        'users': users,
        'emails': emails,
        'item': item,
        'comment': comment,
    }
    return render(request, 'admin2.html', context)

@login_required(login_url='aadmin_login')
def users(request):
    users = Users.objects.all().order_by('-id')
    users = Users.objects.filter(is_superuser=False)
    context = {
        'users': users
    }
    return render(request, 'staff.html', context)

@login_required(login_url='aadmin_login')
def edit_user(request, pk):
    edit = Users.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        gender = request.POST['gender']

        edit.username = name
        edit.address = address
        edit.phone = phone
        edit.email = email
        edit.gender = gender

        edit.save()
        # edit_name.save()
        messages.success(request, 'Update Successfully')
        return redirect('users')
    context = {
        'edit': edit,
    }
    return render(request, 'editstaff.html', context)

@login_required(login_url='aadmin_login')
def delete_user(request, pk):
    delete = Users.objects.get(id=pk)
    if request.method == 'POST':
        delete.delete()
        return redirect('users')
    context = {
        'delete': delete
    }
    return render(request, 'deletestaff.html', context)

@login_required(login_url='aadmin_login')
def varify(request, pk):
    item = Items.objects.get(id=pk)
    if request.method == 'POST':

        if item.delivered:
            item.delivered = False
            item.save()
            return redirect('users')

        item.delivered = True
        item.save()
        return redirect('item')
    context = {
        'item': item,
    }
    return render(request, 'varify.html', context)

@login_required(login_url='aadmin_login')
def item(request):
    item = Items.objects.all().order_by('-id')
    context = {
        'item': item,
    }
    return render(request, 'items.html', context)

@login_required(login_url='aadmin_login')
def edit_item(request, pk):
    item = Items.objects.get(id=pk)
    if request.method == 'POST':
        sender_number = request.POST['s_number']
        sender_address = request.POST['s_address']
        sender_name = request.POST['s_name']

        receiver_number = request.POST['r_number']
        receiver_address = request.POST['r_address']
        receiver_name = request.POST['r_name']

        item.sender_name = sender_name
        item.sender_address = sender_address
        item.sender_number = sender_number
        item.receiver_name = receiver_name
        item.receiver_address = receiver_address
        item.receiver_number = receiver_number

        item.save()
        return redirect('item')

    context = {
        'item': item,
    }
    return render(request, 'edititem.html', context)

@login_required(login_url='aadmin_login')
def delete_item(request, pk):
    item = Items.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item')
    context = {
        'item': item,
    }
    return render(request, 'deleteitem.html', context)

@login_required(login_url='aadmin_login')
def new_item(request):

    uni = 'LOGISTIC'
    rand1 = str(random.randint(1000, 9999))
    ticket = uni + rand1
    # ticket = int(ticket)
    while len(Items.objects.filter(booking_mode=ticket)) != 0:
        rand1 = str(random.randint(1000, 9999))
        ticket = uni + rand1
        ticket = int(ticket)

    if request.method == 'POST':
        sender_number = request.POST['sender_number']
        sender_address = request.POST['sender_address']
        sender_name = request.POST['sender_name']

        receiver_number = request.POST['receiver_number']
        receiver_address = request.POST['receiver_address']
        receiver_name = request.POST['receiver_name']

        weight = request.POST['weight']
        pickup_time = request.POST['pickup_time']
        pickup_date = request.POST['pickup_date']
        destination = request.POST['destination']
        freight = request.POST['freight']
        item = request.POST['item']
        qnty = request.POST['qnty']
        booking_mode = ticket

        items = Items.objects.create(
                sender_number=sender_number, sender_name=sender_name, sender_address=sender_address,
                receiver_number=receiver_number, receiver_name=receiver_name, receiver_address=receiver_address,
                item=item, weight=weight, pickup_time=pickup_time, pickup_date=pickup_date, booking_mode=booking_mode,
                destination=destination, freight=freight, qnty=qnty,
            )
        items.save()
        messages.success(request, 'Registration successfully')
        return redirect('item')
    context = {}
    return render(request, 'newitem.html', context)

@login_required(login_url='aadmin_login')
def message(request):
    emails = Message.objects.all().order_by('-id')
    context = {
        'emails': emails
    }
    return render(request, 'messages.html', context)

@login_required(login_url='aadmin_login')
def delete_message(request, pk):
    emails = Message.objects.get(id=pk)
    if request.method == 'POST':
        emails.delete()
        return redirect('message')
    context = {
        'emails': emails
    }
    return render(request, 'deletemessage.html', context)

@login_required(login_url='aadmin_login')
def comment(request):
    if request.method == ('POST'):
        name = request.POST['name']
        message = request.POST['message']

        comment = Comment.objects.create(name=name, message=message)
        comment.save()
        messages.success(request, 'mail was successfully sent')
        return redirect('comment')
    comment = Comment.objects.all().order_by('-id')
    context = {
        'comment': comment
    }
    return render(request, 'comment.html', context)

@login_required(login_url='aadmin_login')
def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('comment')
    context = {
        'comment': comment,
    }
    return render(request, 'deletecomment.html', context)

@login_required(login_url='aadmin_login')
def new_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        number = request.POST['number']
        address = request.POST['address']
        gender = request.POST['gender']

        if password1 == password2:
            if Users.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('new_user')
            elif Users.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('new_user')
            else:
                user = Users.objects.create_user(username=username, email=email, password=password1,
                                                number=number, gender=gender, address=address)
                user.save()
                messages.success(request, 'account was created successfully')
                return redirect('users')
        else:
            messages.info(request, 'password not matching...')
            return redirect('new_user')
    context = {
        'message': messages,
    }
    return render(request, 'newuser.html', context)


