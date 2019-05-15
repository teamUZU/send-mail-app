from django.shortcuts import render
from django.shortcuts import redirect
from .models import Client
from .models import User
from .forms import ClientForm
from .forms import UserForm
from .forms import CreateclientForm
from .forms import CreateuserForm
from .forms import EditclientForm # editclientで追記
from .forms import EdituserForm
from .forms import SendmailclientForm
from .forms import SendmailuserForm
from .forms import BroadcastclientForm # broadcastclientで追記
from .forms import BroadcastuserForm
from django.core.mail import send_mail # メール送信部分で追記
from mailing_list import settings # メール送信部分で追記
from django.contrib import messages # フラッシュメッセージ表示のために追記

# frontpageのビュー関数
def frontpage(request):
	params = {
		'login_account':request.user,
	}
	return render(request, 'list_app/frontpage.html', params)

# clientpageのビュー関数
def client(request):
    params = {
        'login_account':request.user,
        'form':ClientForm(),
        'data':[],
    }
    if (request.method == 'POST'):
        c_name = request.POST['search_name']
        params['data'] = Client.objects.filter(name__contains=c_name)
        params['form'] = ClientForm(request.POST)
    else:
        params['data'] = Client.objects.all()
    return render(request, 'list_app/client.html', params)

# userpageのビュー関数
def user(request):
    params = {
        'login_account':request.user,
        'form':UserForm(),
        'data':[],
    }
    if (request.method == 'POST'):
        c_name = request.POST['name']
        params['data'] = User.objects.filter(name__contains=c_name)
        params['form'] = UserForm(request.POST)
    else:
        params['data'] = User.objects.all()
    return render(request, 'list_app/user.html', params)

# createclientのビュー関数
def createclient(request):
    params = {
        'login_account':request.user,
        'form':CreateclientForm(),
    }
    if (request.method == 'POST'):
        name = request.POST['name']
        tel_number = request.POST['tel_number']
        mail = request.POST['mail']
        regddate = request.POST['regddate']
        status = request.POST['status']
        client = Client(name=name, tel_number=tel_number, mail=mail, regddate=regddate, status=status)
        client.save()
        return redirect(to='client')
    return render(request, 'list_app/createclient.html', params)

# createuserのビュー関数
def createuser(request):
    params = {
        'login_account':request.user,
        'form':CreateuserForm(),
    }
    if (request.method == 'POST'):
        name = request.POST['name']
        tel_number = request.POST['tel_number']
        mail = request.POST['mail']
        regddate = request.POST['regddate']
        status = request.POST['status']
        user = User(name=name, tel_number=tel_number, mail=mail, regddate=regddate, status=status)
        user.save()
        return redirect(to='user')
    return render(request, 'list_app/createuser.html', params)

# editclientのビュー関数
def editclient(request, num):
    obj = Client.objects.get(id=num)
    if (request.method == 'POST'):
        client = EditclientForm(request.POST, instance=obj)
        if client.is_valid():
            client.save()
        return redirect(to='client')
    params = {
        'login_account':request.user,
        'form':EditclientForm(instance=obj),
        'id':num,
    }
    return render(request, 'list_app/editclient.html', params)

# edituserのビュー関数
def edituser(request, num):
    obj = User.objects.get(id=num)
    if (request.method == 'POST'):
        user = EdituserForm(request.POST, instance=obj)
        if user.is_valid():
            user.save()
        return redirect(to='user')
    params = {
        'login_account':request.user,
        'form':EdituserForm(instance=obj),
        'id':num,
    }
    return render(request, 'list_app/edituser.html', params)

# sendmailclientのビュー関数
def sendmailclient(request, num):
    obj = Client.objects.get(id=num)
    params = {
        'login_account':request.user,
        'form':SendmailclientForm(instance=obj),
        'id':num,
    }
    if (request.method == 'POST'):
        subject = request.POST['subject']
        message = request.POST['message']
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [
            request.POST['mail'],
        ]
        send_mail(subject, message, from_email, recipient_list)
        messages.success(request, 'メールの送信が完了しました。このウィンドウを閉じてください。') # フラッシュメッセージ表示
    return render(request, 'list_app/sendmailclient.html', params)

# sendmailuserのビュー関数
def sendmailuser(request, num):
    obj = User.objects.get(id=num)
    params = {
        'login_account':request.user,
        'form':SendmailuserForm(instance=obj),
        'id':num,
    }
    if (request.method == 'POST'):
        subject = request.POST['subject']
        message = request.POST['message']
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [
            request.POST['mail'],
        ]
        send_mail(subject, message, from_email, recipient_list)
        messages.success(request, 'メールの送信が完了しました。このウィンドウを閉じてください。') # フラッシュメッセージ表示
    return render(request, 'list_app/sendmailuser.html', params)

# broadcastclientのビュー関数
def broadcastclient(request):
    obj = Client.objects.values_list('mail', flat=True)
    params = {
        'login_account':request.user,
        'form':BroadcastclientForm(),
    }
    if (request.method == 'POST'):
        for val in obj:
            subject = request.POST['subject']
            message = request.POST['message']
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [val,]
            send_mail(subject, message, from_email, recipient_list)
        messages.success(request, 'メールの送信が完了しました。このウィンドウを閉じてください。')
    return render(request, 'list_app/broadcastclient.html', params)

# broadcastuserのビュー関数
def broadcastuser(request):
    obj = User.objects.values_list('mail', flat=True)
    params = {
        'login_account':request.user,
        'form':BroadcastuserForm(),
    }
    if (request.method == 'POST'):
        for val in obj:
            subject = request.POST['subject']
            message = request.POST['message']
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [val,]
            send_mail(subject, message, from_email, recipient_list)
        messages.success(request, 'メールの送信が完了しました。このウィンドウを閉じてください。')
    return render(request, 'list_app/broadcastuser.html', params)