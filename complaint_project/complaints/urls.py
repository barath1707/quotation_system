from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_customer, name='create_customer'),
    path('add_cutomer_quotation', views.add_cutomer_quotation, name='add_cutomer_quotation'),
    path('add_table', views.add_table, name='add_table'),
    path('add_table_headers', views.add_table_headers, name='add_table_headers'),
    path('add_table_value', views.add_table_value, name='add_table_value'),
    path('add_complaint_details', views.add_complaint_details, name='add_complaint_details'),
    path('all_customers', views.all_customers, name='all_customers'),
    path('document_preview', views.document_preview, name='document_preview'),
    path('delete_quotation', views.delete_quotation, name='delete_quotation'),
    path('delete_customer', views.delete_customer, name='delete_customer'),
    path('quotation/<int:quotation_id>/download/', views.download_quotation_doc, name='download_quotation_doc'),
]