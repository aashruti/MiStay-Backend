from django.shortcuts import render
from Userreg.forms import UserForm,UserProfileInfoForm,EventForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.views import View
from .models import Event
def index(request):
    return render(request,'Userreg/index.html')
@login_required
def Cevent(request):
    Created = False
    if request.method == 'POST':
        event_form = EventForm(data=request.POST)
        if event_form.is_valid():
            event = event_form.save()
            event.save()
            Created = True
        else:
            print(event_form.errors)
    else:
        event_form = EventForm()
    return render(request,'Userreg/Cevent.html',
                          {'event_form':event_form,
                           'Created':Created})
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'Userreg/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'Userreg/login.html', {})
# Create your views here.
class EventList(LoginRequiredMixin, generic.ListView):
    model = Event
    template_name = 'Userreg/Eevent.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Event.objects.all()
        else:
            return Event.objects.all()

class EventDetail(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        view = EventDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentCreate.as_view()
        return view(request, *args, **kwargs)

class EventDelete(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Event
    template_name = 'Userreg/delete.html'
    success_url = reverse_lazy('Userreg:Eevent')
    context_object_name = 'event'
    success_message = "%(name)s was deleted successfully"

@login_required()
def attend_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    attendee = User.objects.get(username=request.user)
    event.attendees.add(attendee)
    create_action(attendee, 'is attending', event)
    messages.success(request, 'You are now attending {0}'.format(event.name))
    return redirect('events:event-detail', pk=event.pk)


@login_required()
def not_attend_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    attendee = User.objects.get(username=request.user)
    event.attendees.remove(attendee)
    create_action(attendee, 'no longer attending', event)
    messages.success(request, 'You are no longer attending {0}'.format(event.name))
    return redirect('events:event-detail', pk=event.pk)