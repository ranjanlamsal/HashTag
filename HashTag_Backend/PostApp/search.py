import json
from rest_framework.views import APIView
from rest_framework.response import Response
from PostApp.models import Post


class Get_posts(APIView):
    def get(self, request):
        posts = []
        search_data = json.loads(request.body)
        search = search_data.get('search')

        if search:
            objs = Post.objects.filter(content__contains = search)


            for obj in objs:
                posts.append({
                    'content' : obj.content,
                })

        return Response(
            posts
        )