from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from .models import Profile

# Create your views here.


class PasswordChange(PasswordChangeView):
    # form_class = UserUpdateFor
    template_name = 'registration/password.html'
    success_url = reverse_lazy('blog-home')


class UserRegisterView(SuccessMessageMixin, generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def get_success_message(self, cleaned_data):
        usernamer = cleaned_data.get('username')
        return f'Account has been created for {usernamer}'


name = 'shubham'


class UserEditView(SuccessMessageMixin, generic.UpdateView):
    form_class = UserUpdateForm
    template_name = 'registration/updateuser.html'
    success_url = reverse_lazy('profile')
    # fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def get_success_message(self, cleaned_data):
        usernamer = cleaned_data.get('first_name')
        name = username
        return f'Profile has been updated for {usernamer}'

    def get_object(self):
        return self.request.user


class ProfileCreateView(SuccessMessageMixin, CreateView):
    model = Profile
    template_name = 'registration/createprofile.html'
    success_url = reverse_lazy('profile')
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        usernamer = cleaned_data.get('first_name')
        return f'Profile has been created for {name}'


class ProfileEditView(SuccessMessageMixin, generic.UpdateView):
    form_class = ProfileUpdateForm
    model = Profile
    template_name = 'registration/updateprofile.html'
    # fields = ['image', 'instagram_url', 'bio']
    success_url = reverse_lazy('profile')

    def get_success_message(self, cleaned_data):
        usernamer = cleaned_data.get('first_name')
        return f'Profile has been updated for {name}'

    def get_object(self):
        return self.request.user


# class profile(DetailView):
#     model = Profile
#     template_name = 'registration/profile.html'

#     def get_context_data(self, *args, **kwargs):
#         users = Profile.objects.all()
#         data = super(profile, self).get_context_data(*args, **kwargs)
#         page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
#         data["page_user"] = page_user
#         return data


@login_required
def profile(request):
    return render(request, 'registration/profile.html')
    # if request.method == 'POST':
    #     u_form = UserUpdateForm(request.POST, instance=request.user)
    #     p_form = ProfileUpdateForm(
    #         request.POST, request.FILES, instance=request.user.profile)

    #     if u_form.is_valid() and p_form.is_valid():
    #         u_form.save()
    #         p_form.save()
    #         messages.success(request, f'Your account has been updated')
    #         return redirect('profile')

    # else:
    #     u_form = UserUpdateForm(instance=request.user)
    #     p_form = ProfileUpdateForm(instance=request.user.profile)

    # context = {
    #     'u_form': u_form,
    #     'p_form': p_form,
    # }
