import json
from django.forms.models import model_to_dict

# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Product
from api.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    # request.data => Serializer verify if it meets to serializer requirements => verify the requirements of the model
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        # instance = (
        #     serializer.save()
        # )  # this step will save the data and return the instance itself
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)


# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     """
#     DRF API View
#     """
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         data = ProductSerializer(instance).data
#         # data = model_to_dict(instance, fields=["id", "title", "price", "sale_price"])
#         # data["ttile"] = model_data.title
#         # data["content"] = model_data.content
#         # data["price"] = model_data.price
#     return Response(data)


# def api_home(request, *args, **kwargs):
#     # request -> HttpRequest -> Django
#     # get json from rquest == request.body
#     # request.body is byte string of JSON data


#     body = request.body
#     data = {}
#     try:
#         data=json.loads(body) # sting of JSON data -> Python Dict
#     except:
#         pass
#     print(data)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type

#     data['params'] = dict(request.GET) # url query params
#     return JsonResponse(data)
