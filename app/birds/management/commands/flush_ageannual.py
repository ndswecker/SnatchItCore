from django.core.management.base import BaseCommand
from birds.models import AgeAnnual

class Command(BaseCommand):
    help = "Flushes all data from AgeAnnual model"

    def handle(self, *args, **options):
        count = AgeAnnual.objects.count()
        AgeAnnual.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f"Successfully flushed {count} AgeAnnual objects"))
        