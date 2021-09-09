from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
    """ Test API View """

    serializer_class = serializers.HelloSerializers

    def get(self,request,format=None):
        """Returns the list of API features"""
        an_apiview = [
            'Uses HTTP methods as functions (get,post,patch,put,delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over the applicaton logic',
            'Is mapped manually to the URLs',
        ]
        return Response({'message':'get method','an_apiview':an_apiview})

    def post(self, request):
        """create hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            place = serializer.validated_data.get('place')
            message = {"name":name, "place":place}
            return Response(message)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pl=None):
        """Handling a partial update of the object """
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Deleting an object"""
        return Response({'method':'Delete'})
