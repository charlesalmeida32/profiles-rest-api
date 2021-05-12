from rest_framework.views import APIView
from rest_framework.response import Response



class HelloApiView(APIView):
    """Test API View """
    def get(self, request, format=None):
        an_apiview = [
        'Uses HTTP method funtions (get, post, put , delete, patch)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'It is mapped manually to the URLs'
        ]

        return Response({'message': 'Helle', 'an_apiview': an_apiview})
