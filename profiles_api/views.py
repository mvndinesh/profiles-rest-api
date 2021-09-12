from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


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

    def patch(self,request,pk=None):
        """Handling a partial update of the object """
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Deleting an object"""
        return Response({'method':'Delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API View Set """
    serializer_class = serializers.HelloSerializers
    def list(self,request):
        """Return a singel hello message"""
        a_viewset = [
            'uses actions (list,create,retreive,update,partial_update)',
            'Automatically maps to URLs using routers',
            'provides more functionality with less code',
        ]
        return Response({'message':'Hello!', 'a_viewset':a_viewset})

    def create(self, request):
        "create a new hello message"
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            place = serializer.validated_data.get('place')
            return_dict = {"message":"created message","name":name,"place":place}
            return Response(return_dict,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """ Handling getting an object by its ID"""
        return Response({"retrieve_get":'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = permissions.UpdateOwnProfile
