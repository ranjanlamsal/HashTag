import 'package:flutter/material.dart';
import 'package:untitled/api/auth/auth_api.dart';
import 'package:untitled/api/post_api.dart';
import 'package:untitled/constant.dart';
import 'package:untitled/pages/login.dart';

import '../api/tag_api.dart';
import '../models/post_model.dart';
import '../models/tag_model.dart';



class Profile extends StatefulWidget {
  const Profile({Key? key}) : super(key: key);

  @override
  State<Profile> createState() => _ProfileState();
}

class _ProfileState extends State<Profile> {
  late List<Tag> self_tags = [];
  late List<Post> selfposts = [];
  @override
  void initState()
  {
    super.initState();
    selfposts = [];
    self_tags =[];
    getSelfPost().then((value)
    {
      setState(() {
        selfposts=value;
      });
    });
    getSelf_tag().then((value)
    {
      {
        setState(() {
          self_tags=value;
        });
      }});
  }
  
  
  @override
  Widget build(BuildContext context) {
    
    double screen_width = MediaQuery.of(context).size.width;
    double screen_height = MediaQuery.of(context).size.height;


    return Scaffold(
      backgroundColor: Color.fromARGB(255, 202,207,250),
      appBar: AppBar(
        backgroundColor:Color.fromARGB(255, 202,207,250),
        elevation: 1,
        // leading: IconButton(
        //   icon: Icon(Icons.arrow_back),
        //   color: Colors.black,
        //   onPressed: (){
        //     // Navigator.pushNamed(context, 'home');
        //   },
        // ),
       
        // ),
        
        centerTitle: false,
        actions: [
          // IconButton(onPressed: (){}, icon: Icon(Icons.dehaze), color: Colors.black),


          
        ],
        
        ),
        drawer: Drawer(backgroundColor: drawer_color,
        child: ListView(
          children:[ 
            DrawerHeader(child: Text("HashTag")),
            ListTile(
            title: Text("Logout"),
            onTap: () {
             
              logout();
              Navigator.push(context, MaterialPageRoute(builder: (context)=>const MyLogin()));
            },
          ),
        ])),
        body: Column(
          children: [
            // SizedBox(height: 10),
            
            Text("Posts",style: 
            TextStyle(color: Colors.black,fontSize: 28,fontWeight: FontWeight.w800),),
            // Expanded(child: TagList(self_tags: self_tags),),
            Expanded(
              child: SelfPostList(selfposts: selfposts),
            )
          ]),


      );

  }
}
class TagList extends StatelessWidget {
  final List<Tag> self_tags;

  TagList({required this.self_tags});

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      shrinkWrap: true,
      key: UniqueKey(),
      itemCount: self_tags.length,
      itemBuilder: (BuildContext context, int index) {
        return Container(
          key: ValueKey(self_tags[index].id),
          margin: EdgeInsets.only(top: 20),
          padding: EdgeInsets.all(10),
        child: Column(
          children: [
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text("#"+self_tags[index].title.toString(),
                style: TextStyle(
                  color: Colors.black,fontSize: 12
                ),),
              ],
            ),
          ],
        )
        );
      },
    );
  }
}

class SelfPostList extends StatelessWidget {
  final List<Post> selfposts;
  SelfPostList({Key? key, required this.selfposts}) : super(key: key);

  @override
  Widget build(BuildContext context) {
   return ListView.builder(
      key: UniqueKey(),
      itemCount: selfposts.length,
      itemBuilder: (BuildContext context, int index) {
        return Container(
          
          key: ValueKey(selfposts[index].id),
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
              Text("# "+ selfposts[index].tag_name.toString(),
                style:TextStyle(
                  color: Colors.black,fontSize: 24,fontWeight: FontWeight.w500
                ),
              ),
              Text(selfposts[index].posted_by_user.toString(), style: TextStyle(
                color: Colors.grey,fontSize: 10,
              ),),
              Text(selfposts[index].created_at.toString(),
                style: TextStyle(
                  color: Colors.grey,fontSize: 10,
                ),),
              SizedBox(
                height:10,
              ),
              Text(selfposts[index].content.toString(),style: TextStyle(color: Colors.black,fontSize: 14,
                    ),   

          ),
          SizedBox(height: 10,)],
          //       ),
          ));
            }
  
        );
    
    
  }
}
