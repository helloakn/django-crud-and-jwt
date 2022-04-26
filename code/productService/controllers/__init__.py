from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
#from ..models.productModel import Product
from productService.models.productModel import Product
print(Product)
print('product workds')
class ProductViews(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        print('product post workds')
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "success", 
                    "data": serializer.data
                }, 
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                "status": "error", 
                "data": serializer.errors
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
    #get list or get by id
    def get(self, request, id=None):
        print('here we go, it works')
        print(id)
        if id:
            print('akn ret')
            #item = Product.objects.get(id=id)
            item = get_object_or_404(Product, id=id)
            serializer = ProductSerializer(item)
            return Response(
                {
                    "status": "success", 
                    "data": serializer.data
                }, 
                status=status.HTTP_200_OK
            )

        items = Product.objects.all()
        serializer = ProductSerializer(items, many=True)
        return Response(
            {
                "status": "success", 
                "data": serializer.data
            }, 
            status=status.HTTP_200_OK
        )

    def patch(self, request, id=None):
        #item = Product.objects.get(id=id)
        item = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "success", 
                    "data": serializer.data
                }
            )
        else:
            return Response(
                {
                    "status": "error", 
                    "data": serializer.errors
                }
            )

    def delete(self, request, id=None):
        item = get_object_or_404(Product, id=id)
        item.delete()
        return Response(
            {
                "status": "success", 
                "data": "Item Deleted"
            }
        )