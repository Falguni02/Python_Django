from django.urls import path

from . import views

##### For Class Based views #####

urlpatterns = [
    path('', views.product_list_create_view),
    path('<int:pk>/update/', views.product_update_view),
    path('<int:pk>/delete/', views.product_delete_view),
    path('<int:pk>/', views.product_detail_view)
]

##### For Function Based views #####

# urlpatterns = [
#     path('', views.product_alt_view),
#     # path('<int:pk>/update/', views.product_update_view),
#     # path('<int:pk>/delete/', views.product_delete_view),
#     path('<int:pk>/', views.product_alt_view)
# ]

##### For Mixin views #####

# urlpatterns = [
#     path('', views.product_mixin_view),
#     # path('<int:pk>/update/', views.product_update_view),
#     # path('<int:pk>/delete/', views.product_delete_view),
#     path('<int:pk>/', views.product_mixin_view)
# ]
