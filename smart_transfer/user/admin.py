from django.contrib import admin
from .models import User, PlayerProfile, ClubProfile, ManagerStaffProfile, PlayerAgentProfile, RecruitingAgentProfile, ServiceProviderProfile, SportingManagementAgencyProfile, CommunicationBoxProfile, FitnessClubProfile, EquipmentSupplierProfile, SportsClothingBrandProfile, TravelingAgencyProfile, SponsorProfile
from django import forms

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'user_type', 'is_active', 'is_staff', 'date_joined')
    search_fields = ['email', 'user_type']

class PlayerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'position', 'club')
    search_fields = ('user__email', 'first_name', 'last_name')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(user_type='PLAYER')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class ClubProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'league')
    search_fields = ('user__email', 'name', 'league')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(user_type='CLUB')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class ManagerStaffProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'role', 'club')
    search_fields = ('user__email', 'first_name', 'last_name')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(user_type='MANAGER_STAFF')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class PlayerAgentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'agency_name')
    search_fields = ('user__email', 'first_name', 'last_name')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(user_type='PLAYER_AGENT')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class RecruitingAgentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'agency_name')
    search_fields = ('user__email', 'first_name', 'last_name')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(user_type='RECRUITING_AGENT')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class ServiceProviderProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'service_type')
    search_fields = ('user__email', 'first_name', 'last_name')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(user_type='SERVICE_PROVIDER')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class SportingManagementAgencyProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'agency_name')
    search_fields = ('user__email', 'first_name', 'last_name')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(user_type='SPORTING_MANAGEMENT_AGENCY')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class CommunicationBoxProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'company_name')
    search_fields = ('user__email', 'first_name', 'last_name')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(user_type='COMMUNICATION_BOX')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class FitnessClubProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'name', 'location')
    search_fields = ('user__email', 'first_name', 'last_name')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(user_type='FITNESS_CLUB')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class EquipmentSupplierProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'company_name', 'product_type')
    search_fields = ('user__email', 'first_name', 'last_name')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(user_type='EQUIPMENT_SUPPLIER')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class SportsClothingBrandProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'brand_name')
    search_fields = ('user__email', 'first_name', 'last_name')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(user_type='SPORTS_CLOTHING_BRAND')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class TravelingAgencyProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'agency_name', 'services_offered')
    search_fields = ('user__email', 'first_name', 'last_name')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(user_type='TRAVELING_AGENCY')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class SponsorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'company_name', 'industry')
    search_fields = ('user__email', 'first_name', 'last_name')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(user_type='SPONSOR')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

# Registering the models and their admins
admin.site.register(User, UserAdmin)
admin.site.register(PlayerProfile, PlayerProfileAdmin)
admin.site.register(ClubProfile, ClubProfileAdmin)
admin.site.register(ManagerStaffProfile, ManagerStaffProfileAdmin)
admin.site.register(PlayerAgentProfile, PlayerAgentProfileAdmin)
admin.site.register(RecruitingAgentProfile, RecruitingAgentProfileAdmin)
admin.site.register(ServiceProviderProfile, ServiceProviderProfileAdmin)
admin.site.register(SportingManagementAgencyProfile, SportingManagementAgencyProfileAdmin)
admin.site.register(CommunicationBoxProfile, CommunicationBoxProfileAdmin)
admin.site.register(FitnessClubProfile, FitnessClubProfileAdmin)
admin.site.register(EquipmentSupplierProfile, EquipmentSupplierProfileAdmin)
admin.site.register(SportsClothingBrandProfile, SportsClothingBrandProfileAdmin)
admin.site.register(TravelingAgencyProfile, TravelingAgencyProfileAdmin)
admin.site.register(SponsorProfile, SponsorProfileAdmin)