#  Department Store using Django-
## Problem Statement:

**Create a CRUD ( Create, Read, Update, Delete)  API service for a simple Department Store database using Python Flask or Django Framework. You can use any SQL database (SQLite preferred) for this project.

Use Python 3.7 or above.

A sample schema may look like –

i. Metadata table – (id,  name, address, contact, proprietor name, etc. )

ii. Categories –  ( id, name, description, etc. )   # Example: food & beverage, hardware, art, toiletries, kitchen essentials, etc.

iii.Items - ( id, name, description, marked_price, etc. ) # Items under each category; Items and Categories are related – Each category can multiple items ( One-to-Many )

iv. Suppliers (id, name, address, contact, etc. ) # Suppliers are related to items in Many-to-Many relationship – an item can come from multiple suppliers and a supplier can provide multiple items**

## Implementation:
Successfully implemented CRUD operations on Item, Category and Supplier tables.

### Technonlogies used:
1. Python 3.9
2. Django 4.1.4 
3. Django Rest Framework
4. SqLite3 RDBMS

### API endpoints
1. Item CRUD APIs:

  > /api/items : List/Create items.
  
  > /api/item/<id> : Get/Update/Delete item by id, based on request method.
  
2. Category APIs:

  > /api/categories : List/Create  categories.
  
  > /api/category/<id> : Get/Update/Delete category by id, based on request method.[ Not implemented yet]
  
3. Suppliers APIs:
  
  > api/suppliers/ : List all Suppliers
  
  > api/supplier/<int:pk>/detail : Get suplier by ID.
  
  > api/supplier/create/ : Create Supplier.
  
  > api/supplier/<int:pk>/update/ : Update supplier.
  
  > api/supplier/<int:pk>/delete/ : Delete supplier.
  
### Project setup :
  
  Copy the code with:
  
  > git clone <project-url>
  
  Activate Virtual env:
  
  > env\Scripts\activate
  
 Required libraries are added in department_store/requirements.txt, to install run command:
  
  > pip3 install -r /path/to/requirements.txt
  
 Run the server:
  
  > cd department_store/
  
  >  python3 manage.py runserver
   
 
 ### API call output:
  
  1. Template response:
  
  Get Items:
  
  <img width="923" alt="get_items_temp" src="https://user-images.githubusercontent.com/76721836/210322756-87689071-9a64-44dc-9978-228930218fb7.PNG">
  
  Get item by Id:
  
  <img width="927" alt="get_item_temp" src="https://user-images.githubusercontent.com/76721836/210322798-82587b19-0fe6-4c4b-ba9d-78845f75a68f.PNG">
  
  Create Item:
  
  <img width="923" alt="create_item_temp" src="https://user-images.githubusercontent.com/76721836/210323621-35eac844-4b63-4fb8-8ece-f62fa0abb7a0.PNG">
  
  Created item:
  
  <img width="918" alt="created_item_temp" src="https://user-images.githubusercontent.com/76721836/210324171-6971ba79-d78c-48f5-ad8f-1a68b079706c.PNG">
  
  
  
  
  
  2. Postman JSON response [NOTE: api endpoint is now changed to api/items]
  
  Get items:
  
  <img width="865" alt="get_items1" src="https://user-images.githubusercontent.com/76721836/210321401-9f8404c4-d206-4062-a5bc-c440abfeb4e5.PNG">
  
  Get item by Id:
  
  <img width="872" alt="get_item" src="https://user-images.githubusercontent.com/76721836/210321767-244bcfcb-badd-45e4-a81a-cd9668f191b6.PNG">
  
  Create Item:
  
  <img width="881" alt="create_item" src="https://user-images.githubusercontent.com/76721836/210322657-08b64c3e-c992-453f-aa8d-f9d6433b954d.PNG">
  
  Update Item:
  
  <img width="886" alt="update_item" src="https://user-images.githubusercontent.com/76721836/210321828-b4096503-ea8d-4814-89fb-45788a24008a.PNG">
  
  Delete Item:
  
  <img width="896" alt="delete_item" src="https://user-images.githubusercontent.com/76721836/210321873-a037fc6e-c88e-4719-b5b2-5eba27bbd707.PNG">
  
 
 ## References:
 
 [Django](https://docs.djangoproject.com/en/4.1/)
 
 [Class based views](https://www.geeksforgeeks.org/class-based-generic-views-django-create-retrieve-update-delete/?ref=lbp)
 
 
  
