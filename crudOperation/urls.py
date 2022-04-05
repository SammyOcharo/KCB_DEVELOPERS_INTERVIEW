
from django.contrib import admin
from django.urls import path
from Crud.views import AllCards, add_Card_details, account_update, account_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', AllCards, name='All_accounts'),
    path('api/v1/create/', add_Card_details, name='account_details'),
    path('api/v1/update/<int:pk>/', account_update, name='account_update'),
    path('api/v1/delete/<int:pk>/', account_delete, name='delete')
]
