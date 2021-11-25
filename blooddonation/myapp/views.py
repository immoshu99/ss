from django.contrib.auth.models import User
from django.db.models import query
from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from .models import Article, Bloodgroup,Donation,Contact,Profile
from .forms import DonationCreateForm,RequestChangeForm,ContactForm,LoginForm,UserRegistrationForm,UserEditForm,ProfileEditForm,ProfileForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm
from django.views import generic
from .filters import SearchFilter
# Create your views here.


@login_required

def dashboard(request):
  
    
    return render(request,'home/dashboard.html')


@login_required
def request_change(request):
    
    if request.method == 'POST':
        form = RequestChangeForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    else:

        form = RequestChangeForm()

    return render(request,'home/request.html',{'form':form})

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
       
        if user_form.is_valid() and profile_form.is_valid():
            
            
            new_user = user_form.save(commit=False)
            
            
            profile = profile_form.save(commit=False)

            profile.user = new_user


            new_user.set_password(user_form.cleaned_data['password'])
            
            new_user.save()
            profile.save()

       
            return render(request,'home/register_done.html',{'new_user':new_user,})
    
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()
       

    return render(request,'home/register.html',{'user_form':user_form,'profile_form':profile_form})




def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username = cd['username'],password = cd['password'])

            if user is not None:
                login(request,user)
                return render(request,'home/dashboard.html')
            else:
                return HttpResponse('Invalid login')
        
    else:
        form = LoginForm()

    return render (request,'home/login.html',{'form':form})

   

def home(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    else:

        form = ContactForm()

    article = Article.objects.filter(published=True)

    return render (request,'home/home.html',{'article':article,'form':form})

def doner(request):
    if request.method == 'POST':
        form = DonationCreateForm(request.POST)
        if form.is_valid():
            
            form.save()

            return redirect ('/complete')
            
            

    else:
        form = DonationCreateForm()

    return render(request,'home/done.html',{'form':form})

def complete(request):
    return render(request,'home/complete.html')

def aboutus(request):

    return render(request,'home/aboutus.html')

def privacy(request):

    return render(request,'home/privacy.html')


def find(request):

    blood = Bloodgroup.objects.all()

    doner = Profile.objects.all()

    myfilter = SearchFilter(request.GET)

    doner = myfilter.qs
    
    return render(request,'home/find.html',{'doner':doner,'blood':blood,'myfilter':myfilter})
    

'''def search(request):


    

    if request.method == "POST":
        
        city = request.POST['city']

        thana = request.POST['thana']

        blood = request.POST['blood']

        results = Donation.objects.raw("SELECT * FROM myapp_profile WHERE city="+ city +"AND thana="+ thana+"AND blood="+ blood+ "")


        return render (request,'home/search.html',{'results':results})
    else:
        results = Profile.objects.all()
        return render (request,'home/search.html',{'results':results})'''

def for_doner(request):

    return render(request,'home/for_doner.html')


def faq(request):
    return render(request,'home/faq.html')

def goals(request):
    return render(request,'home/goals.html')

class UserEditView(generic.UpdateView):
    form_class = UserEditForm
    
    template_name = 'home/edit.html'
    success_url = reverse_lazy('myapp:dashboard')

    def get_object(self):
        return self.request.user


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance = request.user,data=request.POST)
        profile_form = ProfileEditForm(instance = request.user.profile ,data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user) #ene amr account khuila jaitase edit na hoiya
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'home/editt.html',{'user_form': user_form,'profile_form': profile_form})



