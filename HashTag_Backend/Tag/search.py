import json
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tag
from PostApp.models import Post

class Get_tags(APIView):
    def get(self, request):
        tags = []
        search_data = json.loads(request.body)
        search = search_data.get('search')

        if search: 
            objs = Tag.objects.filter(title__startswith = search)


            for obj in objs:
                tags.append({
                    'title' : obj.title,
                })

        return Response(
            tags
        )
    
