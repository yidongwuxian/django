from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse
from demo.models import User
class UserForm(forms.Form):
    username = forms.CharField()
    uploadImg = forms.FileField()

def reg(request):
    if request.method == "POST":
        uf = UserForm(request.POST,request.FILES)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            uploadImg = uf.cleaned_data['uploadImg']
            user = User()
            user.username = username
            user.uploadImg = uploadImg
            user.save()
            return HttpResponse('upload ok!')
    else:
        uf = UserForm()
    return render_to_response('reg.html',{'uf':uf})