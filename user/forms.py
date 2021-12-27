from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from user.models import UserProfile

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='用户名')
    email = forms.EmailField(max_length=200, label='邮箱')
    first_name = forms.CharField(max_length=100, label='名')
    last_name = forms.CharField(max_length=100, label='姓')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class UserUpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': forms.TextInput(attrs={'class':'input', 'placeholder':'username'}),
            'email': forms.EmailInput(attrs={'class':'input', 'placeholder':'email'}),
            'first_name': forms.TextInput(attrs={'class':'input', 'placeholder':'first_name'}),
            'last_name': forms.TextInput(attrs={'class':'input', 'placeholder':'last_name'}),
        }

CITY = [
    ('纽约州 (NY)', '纽约州 (NY)'),
    ('佛罗里达州（FL）', '佛罗里达州（FL）'),
    ('德州（TX）', '德州（TX）'),
    ('加利福尼亚州（CA）', '加利福尼亚州（CA）'),
    ('其他（others）', '其他（others）'),
]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'country', 'avatar')
        widgets = {
            'phone': forms.TextInput(attrs={'class':'input', 'placeholder':'电话- 可不填'}),
            'address': forms.TextInput(attrs={'class':'input', 'placeholder':'地址- 可不填'}),
            'city': forms.Select(attrs={'class':'input', 'placeholder':'city'}, choices=CITY),
            'country': forms.TextInput(attrs={'class':'input', 'placeholder':'国家- 现居哪国？',}),
            'avatar': forms.FileInput(attrs={'class':'input', 'placeholder':'头像'}),
        }

