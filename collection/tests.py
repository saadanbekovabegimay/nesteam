from rest_framework.test import APITestCase
from .factories import CollectionFactory
from .models import GameCollection



class CollectionsTest(APITestCase):
    def setUp(self):
        self.col_1 = CollectionFactory()
        self.col_2 = CollectionFactory()
        self.col_3 = CollectionFactory()

    def test_get_list_of_3_collections(self):
        response = self.client.get('/collections/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.col_1.name, response.data[0]["name"])
        self.assertEqual(self.col_2.name, response.data[1]["name"])
        self.assertEqual(self.col_3.name, response.data[2]["name"])

    def test_get_one_collection(self):
        response = self.client.get(f'/collections/{self.col_1.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.col_1.name, response.data["name"])

    def test_create_collection(self):
        collection_data = {
            'name': 'New collection'
        }
        response = self.client.post('/collections/', collection_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(collection_data['name'], response.data["name"])

    def test_update_collection(self):
        updated_name = 'New Collection Name'
        response = self.client.put(f'/collections/{self.col_1.pk}/', {'name': updated_name})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_name, response.data["name"])

    def test_delete_collection(self):
        response = self.client.delete(f'/collections/{self.col_1.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(GameCollection.objects.count(),2)
