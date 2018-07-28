from django.test import TestCase
from .models import Workers
from faker import Faker


# Create your tests here.
class SlugTest(TestCase):
    def setUp(self):
        fake = Faker()
        self.worker = Workers()
        self.worker.first_name = "munis"
        self.worker.last_name = "isazade"
        self.worker.email = fake.email()
        self.worker.description = fake.text()
        self.worker.save()

    def test_slug(self):
        self.assertEqual(self.worker.slug, "munis-isazade")
