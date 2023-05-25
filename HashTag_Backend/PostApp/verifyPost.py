from django.shortcuts import get_object_or_404, redirect, render
from .models import Post

from rest_framework.views import APIView
from rest_framework.response import Response

from Tag.models import Tag

from rest_framework import status

from ModelCode.Text2Tag import Generatetag


#Post Verification
# def get_post_tag(post):
#     return post.tag.title

class VerifyPost(APIView):
    def get(self, request, id):
        user = request.user
        post = Post.objects.get(id=id)

        if user != post.posted_by:
            return Response({
                "error": True,
                "error_msg": "You are not authorized to verify this post"
            })
        if post.status == "UNVERIFIED":
            tag_obj = post.tag
            relevant_tags =tag_obj.relevant_tags.split(',')
            print(relevant_tags)
            print(tag_obj.title)
            print(type(tag_obj.title))
            relevant_tags.append(tag_obj.title)

            #Check in Model 
            model_tags = Generatetag(post.content)
            #compare relevant_tags and model_tags
            for model_tag in model_tags:
                for relevant_tag in relevant_tags:
                    # relevant_tag = relevant_tag.lower()
                    print(model_tag.replace(" ", "").lower(),relevant_tag.replace(" ", "").lower())
                    if model_tag.replace(" ", "").lower() == relevant_tag.replace(" ", "").lower():
                        post.status = "VERIFIED"
                        post.save()
                        return Response(
                            {
                                "verification": True,
                                "verification_msg": "Post verified"
                            }
                        )
            return Response(
                            {
                                "verification": False,
                                "verification_msg": "Post unverified"
                            }
                        )
        else:
            return Response(
                {
                    "error": True,
                    "error_msg": "Post already verified"
                },
                status=status.HTTP_400_BAD_REQUEST
            )