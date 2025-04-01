from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

GROUPS = [
    "PLAYER", "CLUB", "MANAGER_STAFF", "PLAYER_AGENT", "RECRUITING_AGENT",
    "SERVICE_PROVIDER", "SPORTING_MANAGEMENT_AGENCY", "COMMUNICATION_BOX",
    "FITNESS_CLUB", "EQUIPMENT_SUPPLIER", "SPORTS_CLOTHING_BRAND",
    "TRAVELING_AGENCY", "SPONSOR","APPLICATION_ADMIN"
]


class Command(BaseCommand):
    help = "Create default user groups"

    def handle(self, *args, **kwargs):
        for group_name in GROUPS:
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Group '{group_name}' created."))
            else:
                self.stdout.write(self.style.WARNING(f"Group '{group_name}' already exists."))
