import 'package:flutter/material.dart';
import '../models/post_model.dart';
import 'home.dart';
class PostsFromTag extends StatelessWidget {
  late  List<Post> posts;
  PostsFromTag({required this.posts});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Second Page'),
      ),
      body: ListView.builder(
        itemCount: posts.length,
        itemBuilder: (context, index) {
          return Card(
            child: Column(
              children: [
                Text("# " + posts[index].tag_name.toString(),
                style:TextStyle(
                    color: Colors.black,fontSize: 24,fontWeight: FontWeight.w500
                  )),
                Text(posts[index].content.toString(),
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