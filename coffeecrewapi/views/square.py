from square import Square
from square.environment import SquareEnvironment
from square.core.api_error import ApiError
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

client = Square(
    environment=SquareEnvironment.SANDBOX,
    token=settings.SQUARE_ACCESS_TOKEN,
)

@csrf_exempt
def get_orders(request):
  try:
    result = client.orders.search(
      location_ids=[
        "L79CTPXJ8AYAR"
      ]
    )
    print(result)
    return JsonResponse(result)
  except ApiError as e:
    print(e.status_code)
