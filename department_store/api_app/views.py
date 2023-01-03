from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.decorators import api_view
# from .models import Items
from rest_framework.parsers import JSONParser
from .serializers import *
from django.http.response import JsonResponse
from django.views import View
from django.http import HttpResponse, HttpResponseServerError
from rest_framework import status


# Class based views for Items CRUD
class ItemList(View):
    """
    Get available items in the store
    Add new item
    """
    def get(self, request):
        items = Items.objects.all().order_by('-name')
        category = Category.objects.all()
        item_serializer = ItemListSerializer(items, many=True)
        cat_serializer = CategorySerializer(category, many=True)
        context = {'items': item_serializer.data,
                   'category': cat_serializer.data}
        # return JsonResponse(item_serializer.data, safe=False) # 'safe=False' for objects serialization
        return render(request, 'api_app/itemhome.html', context)

    def post(self, request):
        # item_data = JSONParser().parse(request)
        item_data = {
            'id': request.POST['id'],
            'name': request.POST['name'],
            'description': request.POST['description'],
            'marked_rate': request.POST['marked_rate'],
            'category': request.POST['category']}
        item_serializer = ItemListSerializer(data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            # return JsonResponse(item_serializer.data, status=status.HTTP_201_CREATED)
            return redirect('/api/items')
        return JsonResponse(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemModify(View):
    """
    Get Item by Id
    Update Item
    Delete Item
    """
    def get(self, request, pk=None):
        item = Items.objects.get(pk=pk)
        item_serializer = ItemListSerializer(item)
        context = {'items': item_serializer.data}
        # return JsonResponse(item_serializer.data)
        return render(request, 'api_app/updateitems.html', context)

    def post(self, request, pk=None):
        # item_data = JSONParser().parse(request)
        item = Items.objects.get(pk=pk)
        if "update" in request.POST:
            item_data = {
                'id': pk,  # request.POST['id'],
                'name': request.POST['name'],
                'description': request.POST['description'],
                'marked_rate': request.POST['marked_rate'],
                'category': request.POST['category']}
            item_serializer = ItemListSerializer(item, data=item_data)
            if item_serializer.is_valid():
                item_serializer.save()
                # return JsonResponse(item_serializer.data)
                return redirect('/api/items')
            return JsonResponse(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if "delete" in request.POST:
            item.delete()
            # return JsonResponse({'message': 'Item was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
            return redirect('/api/items')


# category crud
class CategoryList(View):
    """
    Get all available Categories : api/categories
    Create Category
    """
    def get(self, request):
        category = Category.objects.all()
        cat_serializer = CategorySerializer(category, many=True)
        context = {'category': cat_serializer.data}
        # return JsonResponse(cat_serializer.data, safe=False)
        # 'safe=False' for objects serialization
        return render(request, 'api_app/categoryhome.html', context)

    def post(self, request):
        # cat_data = JSONParser().parse(request)
        cat_data = {
            'id': request.POST['id'],
            'name': request.POST['name'],
            'description': request.POST['description'],
        }
        cat_serializer = CategorySerializer(data=cat_data)
        if cat_serializer.is_valid():
            cat_serializer.save()
            # return JsonResponse(cat_serializer.data, status=status.HTTP_201_CREATED)
            return redirect('/api/categories')
        return JsonResponse(cat_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryModify(View):
    pass


# Supplier db CRUD operations using built-in CBV
class SupplierBase(View):
    """
    Base class to avoid declaring models, fields, success url repeatedly.
    Inherited by other Supplier Crud Classes
    """
    model = Suppliers
    fields = '__all__'
    template_name = 'api_app/suppliers_list.html'
    success_url = reverse_lazy('store:suppliers_list')


class SupplierList(SupplierBase, ListView):
    """List all available suppliers"""
    template_name = 'api_app/suppliers_list.html'


class SupplierDetail(SupplierBase, DetailView):
    """ List Supplier By ID"""
    template_name = 'api_app/supplier_detail.html'


class SupplierCreate(SupplierBase, CreateView):
    """ Create new Supplier """
    template_name = 'api_app/supplier_create.html'


class SupplierUpdate(SupplierBase, UpdateView):
    " Update Existing supplier by ID"
    template_name = 'api_app/supplier_update.html'


class SupplierDelete(SupplierBase, DeleteView):
    """ Delete supplier by ID"""
    template_name = 'api_app/supplier_delete.html'
