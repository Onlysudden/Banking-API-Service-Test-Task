from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.utils import json
from collections import OrderedDict
import status

from banking.models import Offer

class OfferApiTestCase(APITestCase):
    def setUp(self):
        """Входные данные для всех тестов"""

        self.offer_1 = Offer.objects.create(
            bank_name='Банк 1',
            term_min=5,
            term_max=10,
            rate_min=5.0,
            rate_max=7.5,
            payment_min=1000000,
            payment_max=3000000
        )
        self.offer_2 = Offer.objects.create(
            bank_name='Банк 2',
            term_min=3,
            term_max=15,
            rate_min=5.5,
            rate_max=12.5,
            payment_min=1500000,
            payment_max=4000000
        )
    
    def tearDown(self):
        """Удаление всех данных после тестов"""
        return super().tearDown()

    def test_create(self):
        """Тестирование POST запроса"""

        self.assertEqual(2, Offer.objects.all().count())
        url = reverse('offers-list')
        data = {'bank_name': 'Банк 3', 'term_min': 4, 'term_max': 8, 'rate_min': 5.5, 'rate_max': 8.5, 'payment_min': 1500000, 'payment_max': 4000000}
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, Offer.objects.all().count())

    def test_delete(self):
        """Тестирование DELETE запроса"""

        self.assertEqual(2, Offer.objects.all().count())
        url = reverse('offers-detail', args=[4])
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(1, Offer.objects.all().count())

    def test_get(self):
        """Тестирование GET запроса для всех записей"""

        url = reverse('offers-list')
        response = self.client.get(url)
        expected_data = [OrderedDict([('id', 6), ('payment', 0), ('bank_name', 'Банк 1'), ('term_min', 5), ('term_max', 10), ('rate_min', 5.0), ('rate_max', 7.5), ('payment_min', 1000000), ('payment_max', 3000000)]), OrderedDict([('id', 7), ('payment', 0), ('bank_name', 'Банк 2'), ('term_min', 3), ('term_max', 15), ('rate_min', 5.5), ('rate_max', 12.5), ('payment_min', 1500000), ('payment_max', 4000000)])]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

    def test_get_one(self):
        """Тестирование GET запроса для одной записи"""

        url = reverse('offers-detail', args=[8])
        response = self.client.get(url)
        expected_data = {'id': 8, 'payment': 0, 'bank_name': 'Банк 1', 'term_min': 5, 'term_max': 10, 'rate_min': 5.0, 'rate_max': 7.5, 'payment_min': 1000000, 'payment_max': 3000000}
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)
    
    def test_update(self):
        """Тестирование UPDATE запроса"""

        url = reverse('offers-detail', args=[10])
        data = {'bank_name': 'Банк 8', 'term_min': 5, 'term_max': 10, 'rate_min': 6, 'rate_max': 8.5, 'payment_min': 1250000, 'payment_max': 3000000}
        json_data = json.dumps(data)
        response = self.client.patch(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        expected_data = {'id': 10, 'payment': 0, 'bank_name': 'Банк 8', 'term_min': 5, 'term_max': 10, 'rate_min': 6.0, 'rate_max': 8.5, 'payment_min': 1250000, 'payment_max': 3000000}
        self.assertEqual(response.data, expected_data)

    def test_with_payments_all(self):
        """Тестирование GET запроса с данными"""

        url = reverse('offers-list') + '?rate_min=&rate_max=&payment_min=&payment_max=&order=rate_min&price=2000000&deposit=10&term=8'
        response = self.client.get(url)
        expected_data = [OrderedDict([('id', 12), ('payment', 18499), ('bank_name', 'Банк 1'), ('term_min', 5), ('term_max', 10), ('rate_min', 5.0), ('rate_max', 7.5), ('payment_min', 1000000), ('payment_max', 3000000)]), OrderedDict([('id', 13), ('payment', 18539), ('bank_name', 'Банк 2'), ('term_min', 3), ('term_max', 15), ('rate_min', 5.5), ('rate_max', 12.5), ('payment_min', 1500000), ('payment_max', 4000000)])]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

    def test_with_payments_by_order(self):
        """Тестирование order по rate_min"""

        url = reverse('offers-list') + '?rate_min=&rate_max=&payment_min=&payment_max=&order=rate_min&price=2000000&deposit=10&term=8'
        response = self.client.get(url)
        expected_data = [OrderedDict([('id', 14), ('payment', 18499), ('bank_name', 'Банк 1'), ('term_min', 5), ('term_max', 10), ('rate_min', 5.0), ('rate_max', 7.5), ('payment_min', 1000000), ('payment_max', 3000000)]), OrderedDict([('id', 15), ('payment', 18539), ('bank_name', 'Банк 2'), ('term_min', 3), ('term_max', 15), ('rate_min', 5.5), ('rate_max', 12.5), ('payment_min', 1500000), ('payment_max', 4000000)])]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

        url = reverse('offers-list') + '?rate_min=&rate_max=&payment_min=&payment_max=&order=-rate_min&price=2000000&deposit=10&term=8'
        response = self.client.get(url)
        expected_data = [OrderedDict([('id', 15), ('payment', 18539), ('bank_name', 'Банк 2'), ('term_min', 3), ('term_max', 15), ('rate_min', 5.5), ('rate_max', 12.5), ('payment_min', 1500000), ('payment_max', 4000000)]), OrderedDict([('id', 14), ('payment', 18499), ('bank_name', 'Банк 1'), ('term_min', 5), ('term_max', 10), ('rate_min', 5.0), ('rate_max', 7.5), ('payment_min', 1000000), ('payment_max', 3000000)])]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

    def test_with_payments_filter_by_price(self):
        """Тестирование фильтра по размеру ипотеки"""

        url = reverse('offers-list') + '?rate_min=&rate_max=&payment_min=&payment_max=&order=rate_min&price=1250000&deposit=10&term=8'
        response = self.client.get(url)
        expected_data = [OrderedDict([('id', 16), ('payment', 11562), ('bank_name', 'Банк 1'), ('term_min', 5), ('term_max', 10), ('rate_min', 5.0), ('rate_max', 7.5), ('payment_min', 1000000), ('payment_max', 3000000)])]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

    def test_with_payments_filter_by_rate(self):
        """Тестирование фильтра по минимальной и максимальной ставке"""

        url = reverse('offers-list') + '?rate_min=5.5&rate_max=&payment_min=&payment_max=&order=rate_min&price=2000000&deposit=10&term=8'
        response = self.client.get(url)
        expected_data = [OrderedDict([('id', 19), ('payment', 18539), ('bank_name', 'Банк 2'), ('term_min', 3), ('term_max', 15), ('rate_min', 5.5), ('rate_max', 12.5), ('payment_min', 1500000), ('payment_max', 4000000)])]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

        url = reverse('offers-list') + '?rate_min=&rate_max=10&payment_min=&payment_max=&order=rate_min&price=2000000&deposit=10&term=8'
        response = self.client.get(url)
        expected_data = [OrderedDict([('id', 18), ('payment', 18499), ('bank_name', 'Банк 1'), ('term_min', 5), ('term_max', 10), ('rate_min', 5.0), ('rate_max', 7.5), ('payment_min', 1000000), ('payment_max', 3000000)])]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)

    def test_with_payments_filter_by_term(self):
        """Тестирование фильтра по годам"""

        url = reverse('offers-list') + '?rate_min=&rate_max=&payment_min=&payment_max=&order=rate_min&price=2000000&deposit=10&term=4'
        response = self.client.get(url)
        expected_data = [OrderedDict([('id', 21), ('payment', 37463), ('bank_name', 'Банк 2'), ('term_min', 3), ('term_max', 15), ('rate_min', 5.5), ('rate_max', 12.5), ('payment_min', 1500000), ('payment_max', 4000000)])]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)