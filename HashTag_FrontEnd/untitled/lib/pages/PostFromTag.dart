import 'package:flutter/material.dart';
import 'package:untitled/api/tag_api.dart';
import '../models/post_model.dart';
import '../widget/like.dart';
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
        bottom: PreferredSize(
          preferredSize: Size(20,30),

          child: Column(


            children: [


              Text("# " + widget.tag_name,
                style: TextStyle(
                    color: Colors.black,fontSize: 20,fontWeight: FontWeight.w700
                ),
              ),
           SizedBox(
         height:10,
            )
            ],
          ),

        ),

      ),
      body: ListView.builder(
        itemCount: widget.posts.length,
        itemBuilder: (context, index) {
          return Card(
            margin: EdgeInsets.only(top: 20),
            
            child: Padding(
              padding: const EdgeInsets.only(left: 16, right: 16,top: 16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Text("# " + widget.posts[index].tag_name.toString(),
                  // style:TextStyle(
                  //     color: Colors.black,fontSize: 24,fontWeight: FontWeight.w500
                  //   )),
                  // SizedBox(height: 10,),
                  // Text(widget.posts[index].content.toString(),
                  // style: TextStyle(color: Colors.black,fontSize: 14,
                  //     ),),
                  
                   Text(widget.posts[index].posted_by_user.toString(), style: TextStyle(
                  color: Colors.grey,fontSize: 10,
                ),),
                Text(widget.posts[index].created_at.toString(),
                  style: TextStyle(
                    color: Colors.grey,fontSize: 10,
                  ),),
                SizedBox(
                  height:10,
                ),
                Text(widget.posts[index].content.toString(),style: TextStyle(color: Colors.black,fontSize: 14,
                      ), 
                      
          
            ),
            SizedBox(height: 1,),
            Count(postdata: widget.posts[index]),
            
            SizedBox(height: 10,)

                ],
              ),
            ),
          );
        },
      ),
    );
  }
}