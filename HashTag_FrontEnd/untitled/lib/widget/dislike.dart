import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/placeholder.dart';

import '../api/vote.dart';
import '../models/post_model.dart';

class Count_Down extends StatefulWidget {
  late  Post postdata;
  

  @override
  Count_Down({
    Key? key,
    required this.postdata,
  }) : super(key: key);
  @override
  State<Count_Down> createState() => _Count_DownState();
}

class _Count_DownState extends State<Count_Down> {
  @override
  int updated_upvote =0;
  int updated_downvote = 0;
  Widget build(BuildContext context) {
    return Row(
      children: [
        Column(
          children: [
            IconButton(onPressed: ()async{
              var result = await unlikePost(widget.postdata.id.toString());
                          setState((){
                            widget.postdata.upvote_count= result.item1;
                            widget.postdata.downvote_count = result.item2;
                          });


            }, icon:Icon(Icons.arrow_circle_up_rounded) ),
            Text(widget.postdata.downvote_count.toString())
          ],
        ),
        
      ],
    );   
  }}  