from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [

        ]

        return Response({'message': 'hello', 'an_apiview': an_apiview})