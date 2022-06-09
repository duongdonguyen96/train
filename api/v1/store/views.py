from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.v1.store.serializers import StoreResponseSerializers, StoreCreateSerializers, StoreUpdateSerializers
from core.store.models import Store
from funtions import message

from funtions.color_text import color


@api_view(['GET'])
def get_all(request):
    try:
        stores = Store.objects.all()
    except Exception as ex:
        raise APIException(ex)

    serializer = StoreResponseSerializers(stores, many=True)

    print(color.WARNING + "-------------------RAW SQL-----------------" + color.ENDC)
    print(stores.query)
    print(color.WARNING + "-------------------------------------------" + color.ENDC)

    return Response(serializer.data)


@api_view(['GET'])
def detail(request, store_id):
    try:
        store = Store.objects.get(id=store_id)

    except Store.DoesNotExist as ex:
        raise APIException(ex)
    except Exception as ex:
        raise APIException(ex)

    serializer = StoreResponseSerializers(store, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def create(request):
    serializer = StoreCreateSerializers(data=request.data)
    serializer.is_valid(raise_exception=True)

    name = serializer.validated_data['name']
    address = serializer.validated_data['address']

    if Store.objects.filter(name=name).exists():
        raise APIException(message.ERROR_NAME_IS_EXISTED)

    try:
        album = Store.objects.create(name=name, address=address)
    except Exception as ex:
        raise APIException(ex)

    return Response({
        "id": album.id,
        "name": name,
        "address": address
    })


@api_view(['POST'])
def update(request, store_id):
    serializer = StoreUpdateSerializers(data=request.data)
    serializer.is_valid(raise_exception=True)

    name = serializer.validated_data['name']
    address = serializer.validated_data['address']

    if Store.objects.filter(name=name).exists():
        raise APIException(message.ERROR_NAME_IS_EXISTED)

    try:
        store = Store.objects.get(id=store_id)
    except Store.DoesNotExist as ex:
        raise APIException(ex)
    except Exception as ex:
        raise APIException(ex)

    store.name = name
    store.address = address

    store.save()

    return Response(serializer.data)


@api_view(['DELETE'])  # noqa
def delete(request, store_id):
    try:
        store = Store.objects.get(id=store_id)

    except Store.DoesNotExist as ex:
        raise APIException(ex)
    except Exception as ex:
        raise APIException(ex)

    store.delete()

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
