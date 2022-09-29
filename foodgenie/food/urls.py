from unicodedata import name
from django.urls import path
from . import views

app_name='food'
urlpatterns = [
    path("", views.index, name='index'),
    #item details
    path("<int:item_id>/", views.detail, name='detail'),
    #add items
    path("add_item/", views.add_item, name="add_item"),
    #edit item
    path("edit_item/<int:id>/", views.edit_item, name="edit_item"),
    #delete item
    path("delete_item/<int:id>", views.delete_item, name="delete_item")

]
