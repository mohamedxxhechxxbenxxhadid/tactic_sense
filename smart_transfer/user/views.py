from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserForm ,CustomUserLogin
from django.contrib.auth import get_user_model
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin,AccessMixin 
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.forms import modelformset_factory

from .forms import (
    PlayerProfileForm, ClubProfileForm, ManagerStaffProfileForm,
    PlayerAgentProfileForm, RecruitingAgentProfileForm, ServiceProviderProfileForm,
    SportingManagementAgencyProfileForm, CommunicationBoxProfileForm,
    FitnessClubProfileForm, EquipmentSupplierProfileForm,
    SportsClothingBrandProfileForm, TravelingAgencyProfileForm, SponsorProfileForm
)
from .forms import PostForm,CommentForm,PostImageForm
from django.urls import reverse_lazy
from .models import (
    PlayerProfile, ClubProfile, ManagerStaffProfile,
    PlayerAgentProfile, RecruitingAgentProfile,
    ServiceProviderProfile, SportingManagementAgencyProfile,
    CommunicationBoxProfile, FitnessClubProfile,
    EquipmentSupplierProfile, SportsClothingBrandProfile,
    TravelingAgencyProfile, SponsorProfile,Post,Comment,PostImage
)

User = get_user_model()
def home(request):
    form_register = CustomUserForm()
    form_login = CustomUserLogin()
    return render(request, "user/home.html",{"form_register": form_register,"form_login":form_login})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            print(user)
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password')
            return redirect(request.META.get('HTTP_REFERER', '/'))

    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
        else:
            for field in form.errors:
                messages.error(request, form.errors[field][0])
            return redirect(request.META.get('HTTP_REFERER', '/'))
    return redirect('home')

def logout_user(request):
    if(logout(request)):
        return redirect('home')
    return redirect('home')




@login_required
def profile(request):
    user = request.user
    profile_instance = None
    profile_form = None

    profile_map = {
        "PLAYER": (PlayerProfile, PlayerProfileForm),
        "CLUB": (ClubProfile, ClubProfileForm),
        "MANAGER_STAFF": (ManagerStaffProfile, ManagerStaffProfileForm),
        "PLAYER_AGENT": (PlayerAgentProfile, PlayerAgentProfileForm),
        "RECRUITING_AGENT": (RecruitingAgentProfile, RecruitingAgentProfileForm),
        "SERVICE_PROVIDER": (ServiceProviderProfile, ServiceProviderProfileForm),
        "SPORTING_MANAGEMENT_AGENCY": (SportingManagementAgencyProfile, SportingManagementAgencyProfileForm),
        "COMMUNICATION_BOX": (CommunicationBoxProfile, CommunicationBoxProfileForm),
        "FITNESS_CLUB": (FitnessClubProfile, FitnessClubProfileForm),
        "EQUIPMENT_SUPPLIER": (EquipmentSupplierProfile, EquipmentSupplierProfileForm),
        "SPORTS_CLOTHING_BRAND": (SportsClothingBrandProfile, SportsClothingBrandProfileForm),
        "TRAVELING_AGENCY": (TravelingAgencyProfile, TravelingAgencyProfileForm),
        "SPONSOR": (SponsorProfile, SponsorProfileForm),
    }

    profile_model, profile_form_class = profile_map.get(user.user_type, (None, None))

    if profile_model:
        profile_instance = profile_model.objects.filter(user=user).first()
        if request.method == "POST":
            profile_form = profile_form_class(request.POST, request.FILES, instance=profile_instance)
            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                user.finished = True
                user.save()
                return redirect("profile")
        else:
            profile_form = profile_form_class(instance=profile_instance)

    # Prepare profile fields for display
    profile_fields = []
    if profile_instance:
        for field in profile_instance._meta.get_fields():
            if field.concrete and not field.auto_created and field.name != 'user':
                value = getattr(profile_instance, field.name, None)
                profile_fields.append({
                    'name': field.verbose_name.capitalize(),
                    'value': value
                })

    return render(request, "user/profile.html", {
        "form": profile_form,
        "profile_fields": profile_fields,
        "profile_instance": profile_instance,
    })

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'user/post_create.html'
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        PostImageFormSet = modelformset_factory(PostImage, form=PostImageForm, extra=3, max_num=5)
        if self.request.POST:
            data['image_formset'] = PostImageFormSet(self.request.POST, self.request.FILES, queryset=PostImage.objects.none())
        else:
            data['image_formset'] = PostImageFormSet(queryset=PostImage.objects.none())
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        image_formset = context['image_formset']
        form.instance.user = self.request.user
        if image_formset.is_valid():
            self.object = form.save()
            images = image_formset.save(commit=False)
            for image in images:
                image.post = self.object
                image.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def handle_no_permission(self):
        return redirect('home')
    
class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

    def handle_no_permission(self):
        return redirect('register_user')

class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'user/post_detail.html'
    context_object_name = 'post'

    def handle_no_permission(self):
        return redirect('register_user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comments.all().order_by('-created_at')
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object
            comment.save()
            return redirect('post_detail', pk=self.object.pk)
        context = self.get_context_data()
        context['comment_form'] = form
        return self.render_to_response(context)
def post(self, request, *args, **kwargs):
    self.object = self.get_object()
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post = self.object
        comment.save()

        # ✅ HTMX request: return partial comment list (and optionally form)
        if request.headers.get('HX-Request'):
            comments = self.object.comments.all().order_by('-created_at')
            form = CommentForm()  # reset the form after submission
            return render(request, 'user/partials/comment_list.html', {
                'comments': comments,
                'comment_form': form
            })

        # Normal request fallback (non-HTMX)
        return redirect('post_detail', pk=self.object.pk)

    # Form is invalid
    context = self.get_context_data()
    context['comment_form'] = form
    return self.render_to_response(context)

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'

    def handle_no_permission(self):
        return redirect('register_user')
    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'user/post_update.html'
    success_url = reverse_lazy('post_list')

    def handle_no_permission(self):
        return redirect('register_user')