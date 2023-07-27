from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from core.models import Challenges

CREATE_CHALLENGE_URL = reverse('challenges:challenges-list')


class ChallengeAPITests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123'
        )
        self.token = Token.objects.create(user=self.user)
        self.admin = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123'
        )
        self.admin_token = Token.objects.create(user=self.admin)

    def test_unauthenticated_users_cannot_access_api(self):
        # Test unauthenticated user cannot list challenges
        url = reverse('challenges:challenges-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_users_can_list_challenges(self):
        # Test authenticated user can list challenges
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        url = reverse('challenges:challenges-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_users_cannot_create_challenge(self):
        # Test authenticated user cannot create challenge
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {'name': 'Test Challenge', 'difficulty': 5}
        response = self.client.post(CREATE_CHALLENGE_URL, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_users_cannot_update_challenge(self):
        # Test authenticated user cannot update challenge
        challenge = Challenges.objects.create(
            name='Test Challenge', difficulty=5)
        url = reverse('challenges:challenges-detail', args=[challenge.id])
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {'name': 'Updated Challenge', 'difficulty': 7}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_users_cannot_delete_challenge(self):
        # Test authenticated user cannot delete challenge
        challenge = Challenges.objects.create(
            name='Test Challenge', difficulty=5)
        url = reverse('challenges:challenge-detail', args=[challenge.id])
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_users_can_create_challenge(self):
        # Test admin user can create challenge
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        data = {'name': 'Test Challenge', 'difficulty': 5}
        response = self.client.post(CREATE_CHALLENGE_URL, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_admin_users_can_update_challenge(self):
        # Test admin user can update challenge
        challenge = Challenges.objects.create(
            name='Test Challenge', difficulty=5)
        url = reverse('challenges:challenge-detail', args=[challenge.id])
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        data = {'name': 'Updated Challenge', 'difficulty': 7}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_users_can_delete_challenge(self):
        # Test admin user can delete challenge
        challenge = Challenges.objects.create(
            name='Test Challenge', difficulty=5)
        url = reverse('challenges:challenge-detail', args=[challenge.id])
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
