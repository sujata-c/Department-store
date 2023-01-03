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

## API endpoints
1. Item CRUD APIs:

  > api/items : List/Create items.
  
  > api/item/<id> : Get/Update/Delete item by id, based on request method.
  
2. Category APIs:

  > api/categories : List/Create  categories.
  
  > api/category/<id> : Get/Update/Delete category by id, based on request method.[ Not implemented yet]
  
