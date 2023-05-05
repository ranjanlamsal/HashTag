import 'package:flutter/material.dart';
import 'package:sliding_up_panel/sliding_up_panel.dart';
import 'package:untitled/api/auth/auth_api.dart';
import 'package:untitled/api/comment_api.dart';
import 'package:untitled/models/comment_model.dart';
import 'package:untitled/widget/reply.dart';

import '../models/post_model.dart';
import '../models/user_models.dart';
class Comments extends StatefulWidget {
  final Post post;
  Comments({required this.post});

  @override
  State<Comments> createState() => _CommentsState();
}

class _CommentsState extends State<Comments> {
  List<Comment> comments = [];
  late User user;
  TextEditingController commentController = TextEditingController();
  @override
  void initState() {
    super.initState();
    getComment(widget.post.id.toString()).then((value) 
    // getSelf_tag().then((value) 
    {
    
      setState(() {
        comments = value;
        // self_tags = value;
      });
    
    });
    getUser()?.then((value){
      {
        setState(() {
          user = value!;
          
        });
      }
    });
    
    
  }
  
  Widget build(BuildContext context) {
    
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.white,
        leading: BackButton(color: Colors.black,
        onPressed: () => Navigator.pop(context),),
        title: Text("Comments",style: TextStyle(color: Colors.black),),

      ),
      body:Column(
        children: [
          Expanded(
            child: CommentList(comments: comments,)),
            Divider(),
            Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: commentController,
                    
                    decoration: InputDecoration(hintText: "Add a comment..."),
                  ),
                ),
                IconButton(
                  icon:Icon(Icons.send,color: Colors.black,),
                  onPressed: () async{
                      await addComment(widget.post.id.toString(),user.username.toString() ,  commentController.text);
                      List<Comment> updatedComments = await getComment(widget.post.id.toString());
                      setState(() {
                        comments =updatedComments;
                      });
                      commentController.clear();
                    
                  },
                )
                  ],
                )
              ],
            )
        
    );
    
      
    
  }
}


class CommentList extends StatefulWidget {
  final List<Comment> comments;
  
  CommentList({required this.comments});

  @override
  State<CommentList> createState() => _CommentListState();
}

class _CommentListState extends State<CommentList> {
  @override
  
  Widget build(BuildContext context) {
    return ListView.builder(
      key: UniqueKey(),
      itemCount: widget.comments.length,
      itemBuilder: (BuildContext context,int index) {
        return Container(
          key: ValueKey(widget.comments[index].id),
          margin: EdgeInsets.only(top:20),
          padding: EdgeInsets.all(10),
          
          child: Column(
            // crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Column(
                children: [
                  Text(widget.comments[index].commentor_by.toString()),
                  Text(widget.comments[index].comment_time.toString()),
                  Text(widget.comments[index].comment.toString()),
                  TextButton(
                    onPressed:()
                    {
                      Navigator.push(context, MaterialPageRoute(builder: (context)=>
          
          Replies(comment: widget.comments[index])
          ));
          
                    },
                     child: Text("Show Replies"))

                  
                  
                  
                ],
              )
            ],
          ),

        );
      },
    );
  }
}

