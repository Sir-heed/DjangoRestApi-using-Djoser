from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted(request):
    return Response(data="You are seeing this because you're logged in, try logout and refresh the page to test the authentication class.", status=status.HTTP_200_OK)