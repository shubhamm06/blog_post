from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserRegisterForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserChangeForm

# Create your views here.


class UserRegisterView(SuccessMessageMixin, generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def get_success_message(self, cleaned_data):
        usernamer = cleaned_data.get('username')
        return f'Account has been created for {usernamer}'


class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/update.html'
    success_url = reverse_lazy('blog-home')

    def get_object(self):
        return self.request.user


@login_required
def profile(request):
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
    return render(request, 'registration/profile.html')
