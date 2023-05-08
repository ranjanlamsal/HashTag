import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:untitled/api/auth/auth_api.dart';
import 'package:untitled/api/post_api.dart';
import 'package:untitled/api/tag_api.dart';
import 'package:untitled/api/vote.dart';
import 'package:untitled/models/post_model.dart';
import 'package:untitled/models/tag_model.dart';
import 'package:untitled/models/user_cubit.dart';
import 'package:untitled/pages/PostFromTag.dart';
import 'package:untitled/pages/login.dart';
import 'package:untitled/widget/like.dart';

import '../models/user_models.dart';

class Homepage extends StatefulWidget {
  const Homepage({Key? key}) : super(key: key);

  @override
  State<Homepage> createState() => _HomepageState();
}

class _HomepageState extends State<Homepage> {
  
  List<Post> posts = [];
  // bool isliked = false;
  @override
  void initState() {
    super.initState();
    getPost().then((value) 
    // getSelf_tag().then((value) 
    {
    {
      setState(() {
        posts = value;
        // self_tags = value;
      });
    }});
  }
  @override
  Widget build(BuildContext context) {
    
    User user = context.read<UserCubit>().state;
    
    
    return  Scaffold(
        backgroundColor: Color.fromARGB(255, 202,207,250),
         
        appBar: AppBar(
          
      
        
          backgroundColor:Color.fromARGB(255, 202,207,250),
          elevation: 0,
          
          title: Image.asset("assets/logo.png",
          width : 70,
          ),
          
          centerTitle: false,
          actions: [
            IconButton(onPressed: (){}, icon: Icon(Icons.search), color: Colors.black),
            IconButton(onPressed: (){}, icon: Icon(Icons.notifications_active_outlined),color: Colors.indigoAccent),
            
          ],
        ),
    
        body: Column(
          
          children: [
            Expanded(
              child: PostsList(posts: posts,
             )),
          ],
        ),
        // body: TagList(self_tags: self_tags)
        );
        

      
    
  }
   
  }




class PostsList extends StatefulWidget {
  final List<Post> posts;
  
  
  PostsList({required this.posts});
  

  @override
  
  State<PostsList> createState() => _PostsListState();
}

class _PostsListState extends State<PostsList> {
  
  @override
  int updated_upvote =0;
  int updated_downvote = 0;

  @override
  
  Widget build(BuildContext context) {
    
    return ListView.builder(
      key: UniqueKey(),
      itemCount: widget.posts.length,
      itemBuilder: (BuildContext context, int index) {
        return Container(
          
          key: ValueKey(widget.posts[index].id),
          margin: EdgeInsets.only(top: 20),
          padding: EdgeInsets.all(10),
          
          decoration: BoxDecoration(
            border: Border.all(color: Colors.grey),
            // borderRadius: BorderRadius.circular(10),
            color: Colors.white
          ),
          child: Column(
            
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [ 
              GestureDetector(
                onTap: () async{
                  String tag_name = widget.posts[index].tag_name.toString();
                  List<Post> tag_posts = await getTag_Post(tag_name);
                  Navigator.push(context, MaterialPageRoute(builder: (context)=>PostsFromTag(posts:tag_posts, tag_name: tag_name,),),);
                },
                child: Text("# "+ widget.posts[index].tag_name.toString(),
                  style:TextStyle(
                    color: Colors.black,fontSize: 24,fontWeight: FontWeight.w500
                  ),
                ),
              ),
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
          
          SizedBox(height: 10,)],
          //       ),
          ));
            }
  
        );
    
    
  }
}







