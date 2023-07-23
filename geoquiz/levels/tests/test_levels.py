from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from geoquiz.core.models import Level
from geoquiz.user.tests.test_user_api import create_user


class PublicLevelApiTests(TestCase):
    """Test unauthenticated API access."""

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('levels:level-list')

    def test_unauthenticated_access(self):
        """Test that unauthenticated users cannot access the API."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateLevelApiTests(TestCase):
    """Test authenticated API access."""

    def setUp(self):
        self.client = APIClient()
        self.user = create_user(email='user@example.com', password='test123')
        self.client.force_authenticate(self.user)
        self.url = reverse('levels:level-list')

    def test_authenticated_access(self):
        """Test that authenticated users can retrieve a list of levels."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateLevelApiTests(TestCase):
    """Test creating a new level."""

    def setUp(self):
        self.client = APIClient()
        self.admin_user = create_user(
            email='admin@example.com', password='adminpass', is_superuser=True)
        self.client.force_authenticate(self.admin_user)
        self.url = reverse('levels:level-list')
        self.payload = {'name': 'Level 1'}

    def test_create_level_as_admin(self):
        """Test that only admin users can create new levels."""
        response = self.client.post(self.url, self.payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UpdateLevelApiTests(TestCase):
    """Test updating an existing level."""

    def setUp(self):
        self.client = APIClient()
        self.admin_user = create_user(
            email='admin@example.com', password='adminpass', is_superuser=True)
        self.client.force_authenticate(self.admin_user)
        self.level = Level.objects.create(name='Level 1')
        self.url = reverse('levels:level-detail', args=[self.level.id])
        self.payload = {'name': 'Updated Level'}

    def test_update_level_as_admin(self):
        """Test that only admin users can update existing levels."""
        response = self.client.patch(self.url, self.payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteLevelApiTests(TestCase):
    """Test deleting an existing level."""

    def setUp(self):
        self.client = APIClient()
        self.admin_user = create_user(
            email='admin@example.com', password='adminpass', is_superuser=True)
        self.client.force_authenticate(self.admin_user)
        self.level = Level.objects.create(name='Level 1')
        self.url = reverse('levels:level-detail', args=[self.level.id])

    def test_delete_level_as_admin(self):
        """Test that only admin users can delete levels."""
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
