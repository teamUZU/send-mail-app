from django import forms
from .models import Client # EditclientFormで追加,SendmailclientFormでも使う
from .models import User

class ClientForm(forms.Form):
    name = forms.CharField(label='クライアント名')
    tel_number = forms.CharField(label='電話番号')
    mail = forms.EmailField(label='メールアドレス')
    regddate = forms.DateField(label='登録日')
    STATUSES = [
            ('アクティブ', 'アクティブ'),
            ('非アクティブ', '非アクティブ'),
            ('優良', '優良'),
            ('取引終了', '取引終了'),
            ('運営者', '運営者'),
        ]
    status = forms.ChoiceField(label='ステータス', choices=STATUSES)
    
class UserForm(forms.Form):
    name = forms.CharField(label='ユーザー名')
    tel_number = forms.CharField(label='電話番号')
    mail = forms.EmailField(label='メールアドレス')
    regddate = forms.DateField(label='登録日')
    STATUSES = [
            ('アクティブ', 'アクティブ'),
            ('非アクティブ', '非アクティブ'),
            ('優良', '優良'),
            ('利用終了', '利用終了'),
            ('運営者', '運営者'),
        ]
    status = forms.ChoiceField(label='ステータス', choices=STATUSES)

class CreateclientForm(forms.Form):
    name = forms.CharField(label='クライアント名')
    tel_number = forms.CharField(label='電話番号')
    mail = forms.EmailField(label='メールアドレス')
    regddate = forms.DateField(label='登録日')
    STATUSES = [
            ('アクティブ', 'アクティブ'),
            ('非アクティブ', '非アクティブ'),
            ('優良', '優良'),
            ('取引終了', '取引終了'),
            ('運営者', '運営者'),
        ]
    status = forms.ChoiceField(label='ステータス', choices=STATUSES)

class CreateuserForm(forms.Form):
    name = forms.CharField(label='ユーザー名')
    tel_number = forms.CharField(label='電話番号')
    mail = forms.EmailField(label='メールアドレス')
    regddate = forms.DateField(label='登録日')
    STATUSES = [
            ('アクティブ', 'アクティブ'),
            ('非アクティブ', '非アクティブ'),
            ('優良', '優良'),
            ('利用終了', '利用終了'),
            ('運営者', '運営者'),
        ]
    status = forms.ChoiceField(label='ステータス', choices=STATUSES)
    
class EditclientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'tel_number', 'mail', 'regddate', 'status']

class EdituserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'tel_number', 'mail', 'regddate', 'status']

class SendmailclientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['mail']
        widgets = {
            'mail':forms.Textarea
        }
    subject = forms.CharField(label='件名')
    message = forms.CharField(widget=forms.Textarea, label='本文')

class SendmailuserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['mail']
        widgets = {
            'mail':forms.Textarea
        }
    subject = forms.CharField(label='件名')
    message = forms.CharField(widget=forms.Textarea, label='本文')

class BroadcastclientForm(forms.Form):
    subject = forms.CharField(label='件名')
    message = forms.CharField(widget=forms.Textarea, label='本文')

class BroadcastuserForm(forms.Form):
    subject = forms.CharField(label='件名')
    message = forms.CharField(widget=forms.Textarea, label='本文')