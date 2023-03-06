from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import UserProfile


class TestUserProfileSignal(TestCase):
    def test_create_or_update_user_profile(self):
        user = User.objects.create(username='testuser', password='testpass')
        self.assertIsNotNone(user)

        profile = user.userprofile
        self.assertIsInstance(profile, UserProfile)
        self.assertEqual(profile.user, user)

        profile.default_phone_number = '+1234567890'
        profile.default_street_address1 = '123 Main St'
        profile.default_town_or_city = 'Anytown'
        profile.default_postcode = '12345'
        profile.default_country = 'US'
        profile.save()

        profile.refresh_from_db()
        self.assertEqual(profile.default_phone_number, '+1234567890')
        self.assertEqual(profile.default_street_address1, '123 Main St')
        self.assertEqual(profile.default_town_or_city, 'Anytown')
        self.assertEqual(profile.default_postcode, '12345')
        self.assertEqual(profile.default_country, 'US')
