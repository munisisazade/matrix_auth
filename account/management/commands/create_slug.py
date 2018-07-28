from django.core.management import BaseCommand
from account.models import Workers


class Command(BaseCommand):
    help = "Create slug for all Workers model"

    def handle(self, *args, **options):
        print("Started ................>>>>")
        workers = Workers.objects.all()

        for worker in workers:
            if not worker.slug:
                worker.save()
                print("{}".format(worker.slug))

        print("Complate [OK]")
