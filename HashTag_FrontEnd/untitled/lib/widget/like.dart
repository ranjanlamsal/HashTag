// ignore_for_file: public_member_api_docs, sort_constructors_first
import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/placeholder.dart';
import 'package:untitled/models/comment_model.dart';

import '../api/vote.dart';
import '../models/post_model.dart';
import 'comment.dart';

class Count extends StatefulWidget {
  late  Post postdata;
  
  

  @override
  Count({
    Key? key,
    required this.postdata,
  }) : super(key: key);
  State<Count> createState() => _CountState();
}

class _CountState extends State<Count> {
  bool _isLiked = false;
  bool _isUnliked = false;
  @override

  Widget build(BuildContext context) {
    return Row(
      children: [
        Column(
          children: [
            IconButton(
              onPressed: () async {
                if (!_isLiked) {
                  var result = await likePost(widget.postdata.id.toString());
                  setState(() {
                    widget.postdata.upvote_count = result.item1;
                    widget.postdata.downvote_count = result.item2;
                    _isLiked = true;
                    _isUnliked = false;
                  });
                }
                else{
                  var result = await likePost(widget.postdata.id.toString());
                  setState(() {
                    widget.postdata.upvote_count = result.item1;
                    widget.postdata.downvote_count = result.item2;
                    _isLiked = false;
                    _isUnliked = false;
                  });
                }
              },
              icon: Icon(
                _isLiked ? Icons.arrow_upward_sharp : Icons.arrow_circle_up_rounded,
              ),
            ),
            Text(widget.postdata.upvote_count.toString())
          ],
          // children: [
          //   IconButton(onPressed: ()async{
          //     var result = await likePost(widget.postdata.id.toString());
          //                 setState((){
          //                   widget.postdata.upvote_count= result.item1;
          //                   widget.postdata.downvote_count = result.item2;
          //                 });


          //   }, icon:Icon(Icons.arrow_circle_up_rounded) ),
          //   Text(widget.postdata.upvote_count.toString())
          // ],
        ),
        Column(
          children: [
            IconButton(
              onPressed: () async {
                if (!_isUnliked) {
                  var result = await unlikePost(widget.postdata.id.toString());
                  setState(() {
                    widget.postdata.upvote_count = result.item1;
                    widget.postdata.downvote_count = result.item2;
                    _isUnliked = true;
                    _isLiked = false;
                  });
                }
                else{
                  var result = await unlikePost(widget.postdata.id.toString());
                  setState(() {
                    widget.postdata.upvote_count = result.item1;
                    widget.postdata.downvote_count = result.item2;
                    _isUnliked = false;
                    _isLiked = true;
                  });
                }
              },
              icon: Icon(
                _isUnliked ? Icons.arrow_downward_sharp : Icons.arrow_circle_down_rounded,
              ),
              ),
              
            Text(widget.postdata.downvote_count.toString())
          ],
        ),
        IconButton(onPressed: (){
          Navigator.push(context, MaterialPageRoute(builder: (context)=>
          
          Comments(post: widget.postdata)
          ));
          

        }, icon: Icon(Icons.insert_comment_rounded))

      ],
    );   
  }}   
