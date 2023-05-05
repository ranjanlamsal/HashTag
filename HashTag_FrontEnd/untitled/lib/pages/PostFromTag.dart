import 'package:flutter/material.dart';
import 'package:untitled/api/tag_api.dart';
import '../models/post_model.dart';
import 'home.dart';
class PostsFromTag extends StatefulWidget {
  late  List<Post> posts;
  late String tag_name;
  
  PostsFromTag({required this.posts, required this.tag_name});

  @override
  State<PostsFromTag> createState() => _PostsFromTagState();
}

class _PostsFromTagState extends State<PostsFromTag> {
  @override
  
  Widget build(BuildContext context) {
    String condn = "Follow Tag";
    return Scaffold(
      backgroundColor: Color.fromARGB(255, 202,207,250),
      appBar: AppBar(
        backgroundColor:Color.fromARGB(255, 202,207,250),
        elevation: 0,
        centerTitle: false,
        actions: [
          TextButton(onPressed: ()async
          {
            followTag(widget.tag_name);
            
            setState(() {
              condn ="Followed";
            });
            

          }, child: Text(condn))
        ],
      ),
      body: ListView.builder(
        itemCount: widget.posts.length,
        itemBuilder: (context, index) {
          return Card(
            child: Column(
              children: [
                Text("# " + widget.posts[index].tag_name.toString(),
                style:TextStyle(
                    color: Colors.black,fontSize: 24,fontWeight: FontWeight.w500
                  )),
                Text(widget.posts[index].content.toString(),
                style: TextStyle(color: Colors.black,fontSize: 14,
                    ),),
                
              ],
            ),
          );
        },
      ),
    );
  }
}