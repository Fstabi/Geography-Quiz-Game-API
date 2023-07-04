"""
Tests for recipe APIs.
"""
# import tempfile
# import os


# from PIL import Image


from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


from rest_framework import status
from rest_framework.test import APIClient


from core.models import (
    Sfide,
    # Tag,
    # Ingredient,
)


from sfide.serializers import (
    SfideSerializer,
    # SfideDetailSerializer,
)


SFIDE_URL = reverse('sfide:sfide-list')


def detail_url(sfide_id):
    """Create and return an sfide detail URL."""
    return reverse('sfide:sfide-detail', args=[sfide_id])


def create_sfide(user, **params):
    """Create and return an sfide recipe."""
    defaults = {
        'title': 'Sample sfide title',
        'difficulty': 5,
    }
    defaults.update(params)

    sfide = Sfide.objects.create(user=user, **defaults)
    return sfide


class PublicRecipeAPITests(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_sfide(self):
        """Test retrieving a list of sfide."""
        create_sfide(user=self.user)
        create_sfide(user=self.user)

        res = self.client.get(SFIDE_URL)

        sfide = Sfide.objects.all().order_by('-id')
        serializer = SfideSerializer(sfide, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_get_sfide_detail(self):
        """Test get sfide detail."""
        SfideDetailSerializer = create_sfide(user=self.user)

        url = detail_url(Sfide.id)
        res = self.client.get(url)

        serializer = SfideDetailSerializer(Sfide)
        self.assertEqual(res.data, serializer.data)


class PrivateRecipeApiTests(TestCase):
    """Test authenticated API requests."""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='adminpass123',
        )
        self.client.force_authenticate(self.user)

    def test_create_sfide(self):
        """Test creating an sfide."""
        user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='adminpass123',
        )
        self.client.force_authenticate(user=user)

        payload = {
            'title': 'Sample sfide',
            'difficulty': 5,
        }
        res = self.client.post(SFIDE_URL, payload)

        if user.is_superuser:
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)
            sfide = Sfide.objects.get(id=res.data['id'])
            for k, v in payload.sfide():
                self.assertEqual(getattr(sfide, k), v)
            self.assertEqual(sfide.user, user)
        else:
            self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_partial_update_sfide(self):
        """Test updating an sfide partially."""
        user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='adminpass123',
        )
        self.client.force_authenticate(user=user)

        sfide = Sfide.objects.create(
            name='Sample sfide',
            difficulty=5,
        )

        payload = {
            'name': 'Updated sfide',
        }
        url = reverse('sfide-detail', args=[sfide.id])
        res = self.client.patch(url, payload)

        if user.is_superuser:
            self.assertEqual(res.status_code, status.HTTP_200_OK)
            sfide.refresh_from_db()
            self.assertEqual(sfide.name, payload['title'])
        else:
            self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_full_update_sfide(self):
        """Test updating an sfide fully."""
        user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='adminpass123',
        )
        self.client.force_authenticate(user=user)

        sfide = Sfide.objects.create(
            name='Sample sfide',
            difficulty=5,
        )

        payload = {
            'name': 'Updated sfide',
            'difficulty': 7,
        }
        url = reverse('sfide-detail', args=[sfide.id])
        res = self.client.put(url, payload)

        if user.is_superuser:
            self.assertEqual(res.status_code, status.HTTP_200_OK)
            sfide.refresh_from_db()
            for k, v in payload.sfide():
                self.assertEqual(getattr(sfide, k), v)
        else:
            self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_sfide(self):
        """Test deleting an sfide."""
        user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='adminpass123',
        )
        self.client.force_authenticate(user=user)

        sfide = Sfide.objects.create(
            title='Sample sfide',
            difficulty=5,
        )

        url = reverse('sfide-detail', args=[sfide.id])
        res = self.client.delete(url)

        if user.is_superuser:
            self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
            self.assertFalse(Sfide.objects.filter(id=sfide.id).exists())
        else:
            self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
