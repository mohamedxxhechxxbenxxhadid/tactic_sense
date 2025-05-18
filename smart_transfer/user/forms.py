from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Post, Comment, PostImage
User = get_user_model()

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'email',
            'user_type',
            'profile_picture',
            'password1',
            'password2'
        ]

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = ''  
            field.widget.attrs.update({'class': 'form-control'})  


class CustomUserLogin(forms.Form):
    email = forms.EmailField(label="Email", max_length=100)
    password = forms.CharField(
        label="Password",
        max_length=100,
        required=True,
        widget=forms.PasswordInput()
    )

from django import forms
from .models import (
    PlayerProfile, ClubProfile, ManagerStaffProfile, PlayerAgentProfile,
    RecruitingAgentProfile, ServiceProviderProfile, SportingManagementAgencyProfile,
    CommunicationBoxProfile, FitnessClubProfile, EquipmentSupplierProfile,
    SportsClothingBrandProfile, TravelingAgencyProfile, SponsorProfile
)

class BaseProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

# Define forms for each profile

class PlayerProfileForm(BaseProfileForm):
    class Meta:
        model = PlayerProfile
        fields = ['first_name', 'last_name', 'position', 'club']

class ClubProfileForm(BaseProfileForm):
    class Meta:
        model = ClubProfile
        fields = ['name', 'league']

class ManagerStaffProfileForm(BaseProfileForm):
    class Meta:
        model = ManagerStaffProfile
        fields = ['first_name', 'last_name', 'role', 'club']

class PlayerAgentProfileForm(BaseProfileForm):
    class Meta:
        model = PlayerAgentProfile
        fields = ['first_name', 'last_name', 'agency_name']

class RecruitingAgentProfileForm(BaseProfileForm):
    class Meta:
        model = RecruitingAgentProfile
        fields = ['first_name', 'last_name', 'agency_name']

class ServiceProviderProfileForm(BaseProfileForm):
    class Meta:
        model = ServiceProviderProfile
        fields = ['first_name', 'last_name', 'service_type']

class SportingManagementAgencyProfileForm(BaseProfileForm):
    class Meta:
        model = SportingManagementAgencyProfile
        fields = ['first_name', 'last_name', 'agency_name']

class CommunicationBoxProfileForm(BaseProfileForm):
    class Meta:
        model = CommunicationBoxProfile
        fields = ['first_name', 'last_name', 'company_name']

class FitnessClubProfileForm(BaseProfileForm):
    class Meta:
        model = FitnessClubProfile
        fields = ['first_name', 'last_name', 'name', 'location']

class EquipmentSupplierProfileForm(BaseProfileForm):
    class Meta:
        model = EquipmentSupplierProfile
        fields = ['first_name', 'last_name', 'company_name', 'product_type']

class SportsClothingBrandProfileForm(BaseProfileForm):
    class Meta:
        model = SportsClothingBrandProfile
        fields = ['first_name', 'last_name', 'brand_name']

class TravelingAgencyProfileForm(BaseProfileForm):
    class Meta:
        model = TravelingAgencyProfile
        fields = ['first_name', 'last_name', 'agency_name', 'services_offered']

class SponsorProfileForm(BaseProfileForm):
    class Meta:
        model = SponsorProfile
        fields = ['first_name', 'last_name', 'company_name', 'industry']



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']
