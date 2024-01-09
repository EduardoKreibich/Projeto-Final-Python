from .serializers import AccountSerializer
from rest_framework.generics import CreateAPIView


class AccountView(CreateAPIView):
    serializer_class = AccountSerializer
