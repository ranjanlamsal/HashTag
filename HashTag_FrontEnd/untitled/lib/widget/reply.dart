import 'package:flutter/material.dart';
import 'package:untitled/api/comment_api.dart';
import 'package:untitled/models/comment_model.dart';
import 'package:untitled/models/reply_model.dart';

class Replies extends StatefulWidget {
  final Comment comment;
  const Replies({super.key, required this.comment});

  @override
  State<Replies> createState() => _RepliesState();
}

class _RepliesState extends State<Replies> {
  List<Reply> replies =[];
  @override
  void initState() {
    super.initState();
    getReply(widget.comment.id.toString()).then((value) 
    // getSelf_tag().then((value) 
    {
    {
      setState(() {
        replies = value;
        // self_tags = value;
      });
    }});
  }
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: Column(
        children:[Expanded(child: ReplyList(replies:replies )),
      ]),
    );
  }
}

class ReplyList extends StatelessWidget {
  final List<Reply> replies;
  const ReplyList({super.key, required this.replies});

  @override
  Widget build(BuildContext context) {
    return  ListView.builder(
      key: UniqueKey(),
      itemCount: replies.length,
      itemBuilder: (BuildContext context,int index) {
        return Container(
          key: ValueKey(replies[index].id),
          margin: EdgeInsets.only(top:20),
          padding: EdgeInsets.all(10),
          
          
          child: Column(
            
            children: [
              Text(replies[index].replied_by.toString()),
             
            ],
          ),

        );
      },
    );
  }
}