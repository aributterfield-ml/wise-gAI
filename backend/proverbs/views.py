from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_proverbs(request):
    query = request.GET.get('query', '')
    
    # Dummy response for now
    results = [
        f"Proverb matching '{query}' 1",
        f"Proverb matching '{query}' 2",
        f"Proverb matching '{query}' 3",
    ]
    return Response(results)
