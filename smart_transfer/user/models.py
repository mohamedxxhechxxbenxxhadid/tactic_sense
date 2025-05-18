from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.models import Group
from django.db import models
from django.conf import settings

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, user_type=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, user_type=user_type, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        # Assign user to their respective group
        if user_type:
            group, _ = Group.objects.get_or_create(name=user_type)
            user.groups.add(group)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_type', 'APPLICATION_ADMIN')  # Set default user_type

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = [
        ('PLAYER', 'Player'),
        ('CLUB', 'Club'),
        ('MANAGER_STAFF', 'Manager & Staff'),
        ('PLAYER_AGENT', 'Player Agent'),
        ('RECRUITING_AGENT', 'Recruiting Agent'),
        ('SERVICE_PROVIDER', 'Service Provider'),
        ('SPORTING_MANAGEMENT_AGENCY', 'Sporting Management Agency'),
        ('COMMUNICATION_BOX', 'Communication Box'),
        ('FITNESS_CLUB', 'Fitness Club'),
        ('EQUIPMENT_SUPPLIER', 'Equipment Supplier'),
        ('SPORTS_CLOTHING_BRAND', 'Sports Clothing Brand'),
        ('TRAVELING_AGENCY', 'Traveling Agency'),
        ('SPONSOR', 'Sponsor'),
    ]

    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    user_type = models.CharField(max_length=50, choices=USER_TYPES)
    finished = models.BooleanField(blank=False,default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.email} ({self.get_user_type_display()})"

# Profile models for each user type
class PlayerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="player_profile")
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    club = models.CharField(max_length=100, blank=True, null=True)

class ClubProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="club_profile")
    name = models.CharField(max_length=100, blank=True, null=True)
    league = models.CharField(max_length=100, blank=True, null=True)

class ManagerStaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="manager_staff_profile")
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    club = models.CharField(max_length=100, blank=True, null=True)

class PlayerAgentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="player_agent_profile")
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    agency_name = models.CharField(max_length=100, blank=True, null=True)

class RecruitingAgentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="recruiting_agent_profile")
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    agency_name = models.CharField(max_length=100, blank=True, null=True)

class ServiceProviderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="service_provider_profile")
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    service_type = models.CharField(max_length=100, blank=True, null=True)

class SportingManagementAgencyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="sporting_management_agency_profile")
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    agency_name = models.CharField(max_length=100, blank=True, null=True)

class CommunicationBoxProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="communication_box_profile")
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)

class FitnessClubProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="fitness_club_profile")
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

class EquipmentSupplierProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="equipment_supplier_profile")
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    product_type = models.CharField(max_length=100, blank=True, null=True)

class SportsClothingBrandProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="sports_clothing_brand_profile")
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    brand_name = models.CharField(max_length=100, blank=True, null=True)

class TravelingAgencyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="traveling_agency_profile")
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    agency_name = models.CharField(max_length=100, blank=True, null=True)
    services_offered = models.TextField(blank=True, null=True)

class SponsorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="sponsor_profile")
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
