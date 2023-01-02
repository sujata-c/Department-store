from django.test import TestCase
from django.test import Client
import pytest
from .models import *

@pytest.mark.django_db
def test_items():
    client = Client()
    resp=client.get('/api/store')
    assert resp.status_code == 200

@pytest.mark.django_db
def test_item():
    client = Client()
    resp=client.get('/api/store/4')
    assert resp.status_code == 200

@pytest.mark.django_db
def test_item_model():
    cat=Category.objects.create(id=0,name='test_item',description='testing item')
    assert cat is True

# @pytest.mark.django_db
# def test_item_model():
#     item=Items.objects.create(id=0,name='test_item',description='testing item', marked_rate=34.00,category=1)
#     assert item.get() is True