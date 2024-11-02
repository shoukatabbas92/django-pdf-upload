from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import PDFUploadForm,UserRegistrationForm
from django.http import HttpResponse
from .models import PDF
# Create your views here.

def home(request):

    pdfs = PDF.objects.filter(user=request.user.id)
    return render(request,'pdfs/home.html',{'pdfs':pdfs})





def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request,'pdfs/register.html',{'form':form})
    

@login_required
def  upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf = form.save(commit=False)
            pdf.user = request.user
            pdf.save()
            return redirect('home')
    else:
        form = PDFUploadForm()
    return render(request,'pdfs/upload_pdf.html',{'form':form})

@login_required
def delete_pdf(request,pdf_id):
    pdf = get_object_or_404(PDF,id=pdf_id,user =request.user)
    pdf.delete()
    return redirect('home')

@login_required
def view_pdf(request,pdf_id):
    pdf = get_object_or_404(PDF,id=pdf_id, user=request.user)
    return render(request,'pdfs/view_pdf.html',{'pdf': pdf})
