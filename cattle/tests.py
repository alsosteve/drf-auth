from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Cattle


class CattleTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_cattle = Cattle.objects.create(
            name="rake",
            owner=testuser1,
            description="Better for collecting leaves than a shovel.",
        )
        test_cattle.save()

    
    # class 32
    def test_authentication_required(self):
        self.client.logout()
        url = reverse("cattle_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class CattleTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_cattle = Cattle.objects.create(
            name="rake",
            owner=testuser1,
            description="Better for collecting leaves than a shovel.",
        )
        test_cattle.save()

    def test_cattles_model(self):
        cattle = Cattle.objects.get(id=1)
        actual_owner = str(cattle.owner)
        actual_name = str(cattle.name)
        actual_description = str(cattle.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_description, "Better for collecting leaves than a shovel."
        )

    def test_get_cattle_list(self):
        url = reverse("cattle_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cattles = response.data
        self.assertEqual(len(cattles), 1)
        self.assertEqual(cattles[0]["name"], "rake")

    def test_get_cattle_by_id(self):
        url = reverse("cattle_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cattle = response.data
        self.assertEqual(cattle["name"], "rake")

    def test_create_cattle(self):
        url = reverse("cattle_list")
        data = {"owner": 1, "name": "spoon", "description": "good for cereal and soup"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        cattles = Cattle.objects.all()
        self.assertEqual(len(cattles), 2)
        self.assertEqual(Cattle.objects.get(id=2).name, "spoon")

    def test_update_cattle(self):
        url = reverse("cattle_detail", args=(1,))
        data = {
            "owner": 1,
            "name": "rake",
            "description": "pole with a crossbar toothed like a comb.",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cattle = Cattle.objects.get(id=1)
        self.assertEqual(cattle.name, data["name"])
        self.assertEqual(cattle.owner.id, data["owner"])
        self.assertEqual(cattle.description, data["description"])

    def test_delete_cattle(self):
        url = reverse("cattle_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        cattles = Cattle.objects.all()
        self.assertEqual(len(cattles), 0)