from django.test import TestCase
from login.models import UserProfileInfo as User

class UserProfile_Models_Test(TestCase):
    def setUpTestData(self):
        User.create(first_name='Abc', last_name='Def')

    def test_first_name_label(self):
        user = User.objects.get(id=1)
        field_label = User._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_first_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = User._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_get_absolute_url(self):
        user = User.objects.get(id=1)
        self.assertEquals(User.get_absolute_url(), '/login/user_login/1')
