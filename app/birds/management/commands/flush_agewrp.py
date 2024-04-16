from django.core.management.base import BaseCommand
from birds.models import AgeWRP

class Command(BaseCommand):
    help = "Flushes all data from AgeWRP model"

    def handle(self, *args, **options):
        count = AgeWRP.objects.count()
        AgeWRP.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f"Successfully flushed {count} AgeWRP objects"))