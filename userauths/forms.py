from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User 
from membership.models import *

class UserRegisterForm(UserCreationForm):
    #free_membership = Membership.objects.get(membership_type='Free')
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'validate', 'id':'reg_user_name'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'', 'id':'reg_pass_word', 'onkeyup': 'validate()'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'', 'id':'re_pass_word', 'onkeyup': 'validate()'}))

    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'password1', 
            'password2'
            ]
    
    def save(self):
      user = super().save(commit=False)
      user.save()
      # Creating a new UserMembership
      user_membership = UserMembership.objects.create(user=user, membership=self.free_membership)
      user_membership.save()
      # Creating a new UserSubscription
      user_subscription = Subscription()
      user_subscription.user_membership = user_membership
      user_subscription.save()
      return user