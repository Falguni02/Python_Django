from rest_framework import authentication, generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.authentication import TokenAuthentication

from .models import product
from .permissions import IsStaffEditorPermission
from .serializers import ProductSerializer

# class based views

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer  # serialize the data
    authentication_classes = [
        authentication.SessionAuthentication,
        TokenAuthentication
        
    ]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content = content)

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk' # primary key
product_detail_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # primary key

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # primary key

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

product_delete_view = ProductDeleteAPIView.as_view()

# class ProductListAPIView(generics.ListAPIView):
#     queryset = product.objects.all()
#     serializer_class = ProductSerializer

# product_list_view = ProductListAPIView.as_view()

###### OR ######
###### Mixin views ######## 

class ProductMixinView( mixins.CreateModelMixin,
                        mixins.ListModelMixin, #Provides the ability to craete a query set
                        mixins.RetrieveModelMixin,
                        generics.GenericAPIView):
    
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(args,kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "This is a single view doing cool stuff"
        serializer.save(content = content)

product_mixin_view = ProductMixinView.as_view()

###### OR ######
###### Function based views ######## 


@api_view(['GET', 'POST'])
def product_alt_view(request, pk = None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            #detail view
            obj = get_object_or_404(product, pk = pk)
            data = ProductSerializer(obj, many = False).data
            return Response(data)
        else:
            #list view
            queryset = product.objects.all()
            data = ProductSerializer(queryset,many = True).data
            return Response(data)
    
    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            # instance = serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status = 400)

