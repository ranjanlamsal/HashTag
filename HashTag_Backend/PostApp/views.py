import random
from django.shortcuts import get_object_or_404, redirect, render
from .models import Comment, Post,Reply
from django.http import Http404, HttpResponseBadRequest
from .serializer import CommentSerializer, PostSerializer, ReplySerializer
# from .serializer import CommentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics

from Tag.models import Tag
from User.models import UserProfile
from django.contrib.auth.models import User

from Tag.serializer import TagSerializer
from rest_framework import status
from rest_framework import authentication, permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import generics

from rest_framework.permissions import AllowAny
from rest_framework import viewsets

def get_tag_rules(tag_title):
    tag = Tag.objects.get(title = tag_title)
    return {
        "follow_to_post": tag.follow_to_post,
        "relevant_tags": tag.relevant_tags,
    }

class PostView(APIView):
    #post create view

    parser_classes = [MultiPartParser, FormParser, JSONParser]
    
    def post(self, request, title):
        user = UserProfile.objects.get(username = request.user)
        tag =Tag.objects.get(title = title)
        rules = get_tag_rules(title)

        if rules['follow_to_post']:
                
            followers = tag.get_followers()
            # tag_id = request.data['tag_id']
            # print(tag_id)
            # tag = get_tag(tag_id)
            if(user.username in followers):
                if(tag is not None):
                    serializer = PostSerializer(data=request.data)
                    if serializer.is_valid(raise_exception=ValueError):
                        if rules['relevant_tags']:
                            serializer.save(posted_by = user, tag = tag, status = "UNVERIFIED" )
                            return Response({
                                    "error_msg":"followede and if relevant tag"
                            })
                        serializer.save(posted_by = user, tag = tag, status = "VERIFIED" )
                        return Response({
                                "error_msg":" followed and if notrelevant tag"
                            })
                    return Response(
                            {
                                "error":True,
                                "error_msg": serializer.error_messages
                            },
                            status=status.HTTP_400_BAD_REQUEST
                            )
                return Response(
                    {
                        "error":"Invalid Tag"
                    },
                    status = status.HTTP_400_BAD_REQUEST
                )
            return Response({
                "error":"Follow Tag Before Posting"
            })
        
        else:
            if(user):
                if(tag is not None):
                    serializer = PostSerializer(data=request.data)
                    if serializer.is_valid(raise_exception=ValueError):
                        if rules['relevant_tags']:
                            serializer.save(posted_by = user, tag = tag, status = "UNVERIFIED" )
                            return Response({
                                    "msg":"not and if relevant tag"}
                                )
                        serializer.save(posted_by = user, tag = tag, status = "VERIFIED")
                        return Response({
                                "msg":"not and if not relevant tag"}
                            )
                    return Response(
                            {
                                "error":True,
                                "error_msg": serializer.error_messages,
                            },
                            status=status.HTTP_400_BAD_REQUEST
                            )
                return Response(
                    {
                        "error":"Invalid Tag"
                    },
                    status = status.HTTP_400_BAD_REQUEST
                )
            return Response({
                "error":"Invalid User"
            })

class PostListAPIView(generics.ListAPIView):
    #list post in order of id

    parser_classes = [MultiPartParser]
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]
    permission_classes = [permissions.DjangoModelPermissions]
Post_list_view = PostListAPIView.as_view()

class PostRandomListView(APIView):
    
    
    parser_classes = [MultiPartParser]
    def get(self, request):
        user = UserProfile.objects.get(username = request.user)
        if(user in UserProfile.objects.all()):
            posts = Post.objects.all()
            random_posts = random.sample(list(posts), k = posts.count())
            serializer = PostSerializer(random_posts, many = True)
            return Response(serializer.data)
        return Response({
            "error":"invalid_user"
        })

class TrendingPostbyDate(APIView):
    parser_classes = [MultiPartParser]
    def get(self, request):
        posts = Post.objects.all().order_by('created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class TrendingPostByUpvoteCount(APIView):
    parser_classes = [MultiPartParser]
    def get(self, request):
        posts = sorted(Post.objects.all(), key=lambda i: i.no_of_upvotes(), reverse=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class PostDetailAPIView(generics.RetrieveAPIView):
    parser_classes = [MultiPartParser]
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]
    permission_classes = [permissions.DjangoModelPermissions]
    
Post_detail_view = PostDetailAPIView.as_view()


class SelfPostListCreateView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        user = UserProfile.objects.get(username=request.user)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(posted_by=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {
                "error": True,
                "error_msg": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    def get(self, request):
        user = UserProfile.objects.get(username=request.user)
        posts = Post.objects.filter(posted_by=user)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class SelfPostUpdateView(APIView):
    parser_classes = [MultiPartParser]
    #self post update
    def put(self, request, id):
        post = get_post(id)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if post.posted_by == UserProfile.objects.get(username = request.user):
            serializer = PostSerializer(post, data=request.data,)
            request.data._mutable = True
        
            if serializer.is_valid(raise_exception = ValueError):
                serializer.save()
                return Response(serializer.data)
            return Response(
                   {
                       "error":True,
                       "error_msg": serializer.error_messages,
                   },
                   status=status.HTTP_400_BAD_REQUEST
                   )

        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, id):
        post = get_post(id)
        if not post:
            return Response(
                    {
                        "error": True,
                        "error_msg": "Post not found"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
        if post.posted_by == UserProfile.objects.get(username = request.user):
            post.delete()
            return Response({"success":"post deleted"},
                    status = status.HTTP_200_OK
                )
        return Response(
                {
                    "error": True,
                    "error_msg": "Not your post"
                },
                status = status.HTTP_401_UNAUTHORIZED
            )


def get_tag(id):
    try:
        tag = Tag.objects.get(id=id)
    except Tag.DoesNotExist:
        return False
    return tag

def get_post(id):
    try:
        post = Post.objects.get(id = id)
    except Post.DoesNotExist:
        return False
    return post


class TagPosts(APIView):
    parser_classes = [MultiPartParser]
    #post of a particular tag
    def get(self, request, title):
        user = UserProfile.objects.get(username= request.user)
        if(user):
            tag = Tag.objects.get(title=title)
            posts = Post.objects.filter(tag = tag)
            serializer = PostSerializer(posts, many=True)
            # tagserializer = TagSerializer(tag, many=True)
            return Response(serializer.data)
        return Response({
            "error": "invalid_user"
        })
        
class TotalPostTag(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        tag_data = []
        for tag in tags:
            total_posts = Post.objects.filter(tag=tag).count()
            tag_data.append({
                "tag_title": tag.title,
                "total_posts": total_posts
            })
        tag_data.sort(key=lambda x: x["total_posts"], reverse=True)  # Sort tags by total_posts in descending order
        return Response(tag_data)
    
class TotalPost(APIView):
    
    # def get(self, request):
    #     user = UserProfile.objects.get(username = request.user)
    #     # print(user)
    #     posts = Post.objects.filter(posted_by = user)
    #     serializer = PostSerializer(posts, many=True)
    #     return Response(serializer.data)
    def get(self,request,):
        user = UserProfile.objects.get(username = request.user)
        post_count = Post.objects.filter(posted_by = user).count()
        return Response(post_count);
        



class UserLikedPosts(APIView):
    parser_classes = [MultiPartParser]
    #user liked posts
    def get(self, request):
        user = UserProfile.objects.get(username = request.user)
        posts = Post.objects.filter(upvote_users = user)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

# class UpvoteDownvoteSignal(APIView):
#     def get(self, request):
#         user = UserProfile.objects.get(username = request.user)
        

class UpvotePost(APIView):
    def post(self, request, id):
        user = UserProfile.objects.get(username = request.user)
        post = Post.objects.get(id = id)
        if(user in post.downvote_users.all()):
            post.downvote_users.remove(user)
            post.upvote_users.add(user)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        if(user in post.upvote_users.all()):
            post.upvote_users.remove(user)
            serializer = PostSerializer(post)
            return Response(serializer.data)

        post.upvote_users.add(user)
        serializer = PostSerializer(post)
        return Response(serializer.data)

class DownvotePost(APIView):
    def post(self, request, id):
        user = UserProfile.objects.get(username = request.user)
        post = Post.objects.get(id = id)
        if(user in post.upvote_users.all()):
            post.upvote_users.remove(user)
            post.downvote_users.add(user)
            serializer = PostSerializer(post)
            return Response(serializer.data)
            
        if(user in post.downvote_users.all()):
            post.downvote_users.remove(user)
            serializer = PostSerializer(post)
            return Response(serializer.data)

        post.downvote_users.add(user)
        serializer = PostSerializer(post)
        return Response(serializer.data)


def get_user(user):
    try:
        user = UserProfile.objects.get(username = user)
    except UserProfile.DoesNotExist:
        return None
    return user

class CommentView(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    def get(self, request, id):
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            return Response(
                {
                    "error": True,
                    "error_msg": "Post not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, id):
        """ here id is post id """
        post = get_post(id)
        if not post:
            return Response(
                    {
                        "error": True,
                        "error_msg": "Post not found"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
        data = request.data
        commentor_by = UserProfile.objects.get(username=request.user)
        # self.post_id = id
        serializer = CommentSerializer(data = request.data, remove_fields = ['post'])
        if serializer.is_valid(raise_exception = ValueError):
            comment = serializer.save(post = post, commentor_by=commentor_by)
            return Response(CommentSerializer(comment).data, status = status.HTTP_200_OK)
        return Response(
               {
                   "error":True,
                   "error_msg": serializer.error_messages,
               },
               status=status.HTTP_400_BAD_REQUEST
           )
    
class ReplyView(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    serializer_class = ReplySerializer
    
    # def get(self,request,id):
    #     # try:
    #     #     comment = Comment.objects.get(id = id)
    #     # except Comment.DoesNotExist:
    #     #     return Response(
    #     #         {
    #     #             "error": True,
    #     #             "error_msg": "Post not found"
    #     #         },
    #     #         status=status.HTTP_404_NOT_FOUND
    #     #     )
    #     comment = Comment.objects.get(id =id)
    #     replies = Reply.objects.filter(comment=comment)
    #     serializer = ReplySerializer(replies,many = True)
    #     return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

        
    def get_object(self, pk):
        try:
            return Reply.objects.get(pk=pk)
        except Reply.DoesNotExist:
            raise Http404

    def get(self, request, id=None):
        if id is not None:
            reply = self.get_object(id)
            serializer = ReplySerializer(reply)
            return Response(serializer.data)
        else:
            replies = Reply.objects.all()
            serializer = ReplySerializer(replies, many=True)
            return Response(serializer.data)
    def post(self, request, id):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            reply = get_object_or_404(Comment, id=id)
            serializer.save(reply=reply, replied_by=request.user)
            return Response(ReplySerializer(reply.data), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def put(self, request, id):
    #     """ here id is comment id """
    #     try:
    #         comment = Comment.objects.get(id=id)
    #     except Comment.DoesNotExist:
    #         return Response(
    #                 {
    #                     "error": True,
    #                     "error_msg": "Comment not found"
    #                 },
    #                 status=status.HTTP_404_NOT_FOUND
    #             )
    #     if comment.commented_by == UserProfile.objects.get(username = request.user):
    #         serializer = CommentSerializer(comment, request.data, remove_fields = ['commented_by_user', 'post'])
    #     else:
    #         return Response(
    #                 {
    #                     "error": True,
    #                     "error_msg": "Not commented by you"
    #                 },
    #                 status = status.HTTP_401_UNAUTHORIZED
    #             )

    #     if serializer.is_valid(raise_exception = ValueError):
    #         serializer.save()
    #         return Response(serializer.data, status = status.HTTP_200_OK)
    #     return Response(
    #            {
    #                "error":True,
    #                "error_msg": serializer.error_messages,
    #            },
    #            status=status.HTTP_400_BAD_REQUEST
    #        )

    # def delete(self, request, id):
    #     try:
    #         comment = Comment.objects.get(id=id)
    #     except Comment.DoesNotExist:
    #         return Response(
    #                 {
    #                     "error": True,
    #                     "error_msg": "Comment not found"
    #                 },
    #                 status=status.HTTP_404_NOT_FOUND
    #             )
    #     if comment.commented_by == UserProfile.objects.get(username = request.user):
    #         comment.delete()
    #         return Response({"success":"comment deleted"},
    #                 status = status.HTTP_200_OK
    #             )
    #     return Response(
    #             {
    #                 "error": True,
    #                 "error_msg": "Not commented by you"
    #             },
    #             status = status.HTTP_401_UNAUTHORIZED
    #         )

# comment and reply

# class CommentViewSet(viewsets.ModelViewSet):
#     serializer_class = CommentSerializer
    
#     def get_queryset(self):
#         queryset = Comment.objects.all()
#         post_id = self.request.query_params.get('post_id', None)
#         if post_id is not None:
#             queryset = queryset.filter(post=post_id)
#         return queryset
    
#     def create(self, request, *args, **kwargs):
#     #    post_id = request.data.get('post_id')
#         post_id = request.query_params.get('post_id', None)
#         serializer = CommentSerializer(data=request.data, context={'view': self, 'post_id': post_id})
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

#     def perform_create(self, serializer):
#         serializer.save()
# class CommentListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
    
    

# class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     def post(self, request, *args, **kwargs):
#         post_id = self.kwargs.get('pk')  # get the post id from the URL
#         post = Post.objects.get(id=post_id)  # get the post object using the id
#         serializer = self.get_serializer(data=request.data, context={'post': post})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
# class ReplyListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Reply.objects.all()
#     serializer_class = ReplySerializer

# class ReplyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Reply.objects.all()
#     serializer_class = ReplySerializer

