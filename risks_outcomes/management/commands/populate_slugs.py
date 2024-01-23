from django.core.management.base import BaseCommand
from risks_outcomes.models import Hazard
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Populate slugs for Hazard models'

    def handle(self, *args, **kwargs):
        for hazard in Hazard.objects.all():
            if not hazard.slug:  # Check if slug is empty
                base_slug = slugify(hazard.name) if hazard.name else "unnamed-hazard"
                new_slug = base_slug
                counter = 1

                while Hazard.objects.filter(slug=new_slug).exclude(pk=hazard.pk).exists():
                    new_slug = f"{base_slug}-{counter}"
                    counter += 1

                hazard.slug = new_slug
                hazard.save()

                self.stdout.write(self.style.SUCCESS(f'Successfully updated slug for hazard "{hazard.name}"'))
