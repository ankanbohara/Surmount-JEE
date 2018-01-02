from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User,Singleoption,Morethanone,Notification,Performance,Blog,Contact
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .forms import FeedbackForm,RegistrationForm,LoginForm,ContactForm,BlogForm
import random as randoms
from matplotlib import pylab
from pylab import *
import matplotlib.pyplot as plt
import datetime

# Create your views here
def index(request):
    return render(request,'form/edu2.html')
def aboutus(request):
    return render(request,'form/aboutuseducational.html')
@login_required()
def quizmorethanone(request):
    all_question = list(Morethanone.objects.all())
    randoms.shuffle(all_question)
    if request.method=='POST':
        quiz = all_question
        score = 0
        for quizes in quiz:
            right = quizes.answer
            entered = request.POST.get(str(quizes.id))
            if right == entered:
                score += 1
            else:
                score -= 2
        context = {'score': score}
        return render(request, 'form/resultmulti.html', context)
    return render(request, 'form/quizmultiple.html', {'all_question': all_question[0:10]})
@login_required()
def quizsingle(request):
    all_question = list(Singleoption.objects.all())
    randoms.shuffle(all_question)
    if request.method=='POST':
        per = Performance()
        quiz = all_question
        per.datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        per.user = request.user.username
        score = 0
        for quizes in quiz:
            right = quizes.answer
            entered = request.POST.get(str(quizes.id))
            if right == entered:
                score += 1
        per.score = score
        per.save()

        context = {'score': score}
        return render(request, 'form/result.html', context)
    return render(request,'form/quizsingle.html',{'all_question':all_question[0:10]})
score=0
#def result_page(request):


#def result_pagemulti(request):

def certificate_page(request):
    p=Performance.objects.all()
    for i in p:
        if request.user.username==i.user:
            score=i.score
    context = {'score': score}
    return render(request, 'form/certificate.html', context)
def answerpage(request):
    quiz=Singleoption.objects.all()
    context={'quiz':quiz[0:10]}
    return render(request,'form/answer.html',context)
def answerpagemulti(request):
    quiz=Morethanone.objects.all()
    context = {'quiz':quiz[0:10]}
    return render(request,'form/answermulti.html',context)
def syllabus(request):
    return render(request,"form/syllabusadvance.html")
@csrf_protect
def feedback(request):
    if request.method=="POST":
        fom = FeedbackForm(request.POST)
        if fom.is_valid():
            fom.save()
            return redirect('form:index')
    else:
        fom = FeedbackForm()
    return render(request,'form/feedbackform.html',{'fom':fom})
@csrf_protect
def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('form:index')
    else:
        form=RegistrationForm()
    return render(request,'form/newregistration.html',{'form':form})
def success(request):
    return render(request,'form/success.html')
@csrf_protect
def loginview(request):
    if request.method=="POST":
        fr = LoginForm(request.POST)
        if fr.is_valid():
            fr.save()
            username= request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return render(request,'form/edu2.html')
                else:
                    return HttpResponse("You're account is disabled")
            else:
                return redirect('form:registration')
    else:
        fr=LoginForm()
    return render(request,'form/newlogin.html',{'fr':fr})
@login_required()
def log_out(request):
    logout(request)
    return render(request,'form/edu2.html')

def contact(request):
    if request.method=="POST":
        con = Contact()
        con.firstname = request.POST['firstname']
        con.lastname = request.POST['lastname']
        con.state = request.POST['state']
        con.subject = request.POST['subject']
        con.save()
        return redirect('form:enquiry')
    return render(request,'form/contact.html')
def enquiry(request):
    return render(request,'form/contactsuccess.html')
def blog(request):
    if request.method=="POST":
        bl = Blog()
        bl.title = request.POST['title']
        bl.subject = request.POST['subject']
        bl.username = request.POST['uname']
        bl.text = request.POST['text']
        bl.save()
        return redirect('form:index')
    return render(request,'form/blogform.html')
def viewblogs(request):
    blog = Blog.objects.all()
    return render(request,'form/viewblog.html',{'blog':blog})
def notification(request):
    all_notifications = Notification.objects.all()
    return render(request,'form/notification.html',{'all_notifications':all_notifications})
def performance(request):
    s=[]
    t=[]
    all_performances=Performance.objects.all()
    for perfor in all_performances:
        if perfor.user==request.user.username:
            t.append(perfor.datetime)
            s.append(perfor.score)

    plt.plot(t, s)
    plt.xlabel('Date & Time')
    plt.ylabel('Score')
    plt.title('Your Performance analysis')
    plt.grid(True)
    response = HttpResponse(content_type='image/png')
    pylab.savefig(response, format="png")
    plt.close()
    return response



# dfdf=request.post['name field']

