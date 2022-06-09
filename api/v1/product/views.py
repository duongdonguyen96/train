from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.v1.product.serializers import ProductResponseSerializers, ProductCreateSerializers, ProductUpdateSerializers
from core.product.models import Product
from funtions import message

from funtions.color_text import color


@api_view(['GET'])
def get_all(request):
    try:
        products = Product.objects.all()
    except Exception as ex:
        raise APIException(ex)

    serializer = ProductResponseSerializers(products, many=True)

    print(color.WARNING + "-------------------RAW SQL-----------------" + color.ENDC)
    print(products.query)
    print(color.WARNING + "-------------------------------------------" + color.ENDC)

    return Response(serializer.data)


@api_view(['GET'])
def detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as ex:
        raise APIException(ex)
    except Exception as ex:
        raise APIException(ex)

    serializer = ProductResponseSerializers(product, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def create(request):
    serializer = ProductCreateSerializers(data=request.data)
    serializer.is_valid(raise_exception=True)

    name = serializer.validated_data['name']
    price = serializer.validated_data['price']
    store_id = serializer.validated_data['store_id']

    if Product.objects.filter(name=name).exists():
        raise APIException(message.ERROR_NAME_IS_EXISTED)

    try:
        product = Product.objects.create(name=name, price=price, store_id=store_id)
    except Exception as ex:
        raise APIException(ex)

    return Response({
        "id": product.id,
        "name": name,
        "price": price,
        "store_id": store_id
    })


@api_view(['POST'])
def update(request, product_id):
    serializer = ProductUpdateSerializers(data=request.data)
    serializer.is_valid(raise_exception=True)  # noqa

    price = serializer.validated_data['price']
    name = serializer.validated_data['name']
    store_id = serializer.validated_data['store_id']

    try:
        product = Product.objects.get(id=product_id)

    except Product.DoesNotExist as ex:
        raise APIException(ex)
    except Exception as ex:
        raise APIException(ex)

    product.price = price
    product.name = name
    product.store_id = store_id

    product.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete(request, product_id):
    try:
        product = Product.objects.get(id=product_id)

    except Product.DoesNotExist as ex:
        raise APIException(ex)
    except Exception as ex:
        raise APIException(ex)

    product.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)


"""
    Code API ở đây

"""


@api_view(['GET'])
def get_all_products_1(request):
    """
        Ví dụ đang làm câu 1, và đề bài yêu cầu lấy toàn bộ product =>  tên hàm + tên file trong postman là get_all_products_1

        Ví dụ đang làm câu 2, và đề bài yêu cầu lấy toàn bộ product =>  tên hàm + tên file trong postman là get_all_products_2

    """

    pass
