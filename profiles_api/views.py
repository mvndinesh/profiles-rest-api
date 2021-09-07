from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """ Test API View """

    def get(self,request,format=None):
        """Returns the list of API features"""
        an_apiview = [
            'Uses HTTP methods as functions (get,post,patch,put,delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over the applicaton logic',
            'Is mapped manually to the URLs',
        ]
        return Response({'message':'get method','an_apiview':an_apiview})




