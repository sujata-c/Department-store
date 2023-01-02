from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.decorators import api_view
# from .models import Items
from .serializers import *
from django.http.response import JsonResponse
from django.views import View
from django.http import HttpResponse, HttpResponseServerError
from rest_framework import status


# Class based views for Items CRUD
class ItemList(View):

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
            return redirect('/api/store')
        return JsonResponse(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemModify(View):

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
                return redirect('/api/store')
            return JsonResponse(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if "delete" in request.POST:
            item.delete()
            # return JsonResponse({'message': 'Item was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
            return redirect('/api/store')


# category crud
class CategoryList(View):
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


class SupplierBase(View):
    model = Suppliers
    fields = '__all__'
    template_name = 'api_app/suppliers_list.html'
    success_url = reverse_lazy('store:suppliers_list')


class SupplierList(SupplierBase, ListView):
    template_name = 'api_app/suppliers_list.html'


class SupplierDetail(SupplierBase, DetailView):
    template_name = 'api_app/supplier_detail.html'


class SupplierCreate(SupplierBase, CreateView):
    template_name = 'api_app/supplier_create.html'


class SupplierUpdate(SupplierBase, UpdateView):
    template_name = 'api_app/supplier_update.html'


class SupplierDelete(SupplierBase, DeleteView):
    template_name = 'api_app/supplier_delete.html'
