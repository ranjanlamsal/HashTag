import 'package:flutter/material.dart';
import 'package:untitled/api/tag_api.dart';

import '../models/tag_model.dart';
import '../models/post_model.dart';
import 'PostFromTag.dart';



class Trending extends StatefulWidget {
  const Trending({super.key});

  @override
  State<Trending> createState() => _TrendingState();
}

class _TrendingState extends State<Trending> {
  late List<dynamic> totaltagpost = [];
  @override
  void initState()
  {
    super.initState();
    totaltagpost =[];
    getTotalPostTag().then((value)
    {
      setState(() {
        totaltagpost=value;
      });
    });
   
  }
  
  @override
  Widget build(BuildContext context) {
        return Scaffold(
          
              appBar: AppBar(

        automaticallyImplyLeading: false,
        backgroundColor:Color.fromARGB(255, 202,207,250),
        elevation: 0,
        title: Image.asset("assets/logo.png",
        width : 70,
        ),

        centerTitle: false,
        actions: [
          IconButton(onPressed: (){}, icon: Icon(Icons.search), color: Colors.black),

          IconButton(onPressed: (){}, icon: Icon(Icons.notifications_active_outlined),color: Colors.indigoAccent),
          // Row(
          // children: [
          //   Text('Recommended For You')
          // ],
          // )
        ],
        bottom: PreferredSize(
          preferredSize: Size(20,30),

          child: Column(


            children: [


              Text('Trends For You',
                style: TextStyle(
                    color: Colors.black,fontSize: 20,fontWeight: FontWeight.w700
                ),
              ),
           
            
            ],
          ),

        ),

      ),
      body: Column(
        children: [
          Expanded(child: 
          TotalPostTagList(totalPosttag:totaltagpost),
      )]
      ),
    );
  }
}

class TotalPostTagList extends StatelessWidget {
  final List<dynamic> totalPosttag;
  const TotalPostTagList({super.key, required this.totalPosttag});

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      key: UniqueKey(),
      itemCount: totalPosttag.length,
      itemBuilder: (BuildContext context, int index){
        return Container(
           margin: EdgeInsets.only(top: 5 ),
           padding: EdgeInsets.all(20),
           decoration: BoxDecoration(
            // border: Border.all(color: Colors.grey),
            // borderRadius: BorderRadius.circular(10),
            color: Colors.white
          ),
           child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              SizedBox(height: 5,),
              GestureDetector(
                onTap: ()async{
                  String tag_name = totalPosttag[index]['tag_title'];
                  List<Post> tag_posts = await getTag_Post(tag_name);
                  Navigator.push(context, MaterialPageRoute(builder: (context)=>PostsFromTag(posts:tag_posts, tag_name: tag_name,),),);
                },
                child: Text('# ' + totalPosttag[index]['tag_title'],style: TextStyle(
                 color: Colors.black,fontSize: 20,fontWeight: FontWeight.w500,)),
              ),
              SizedBox(height:2),              
              Text('${totalPosttag[index]["total_posts"]} posts', style: TextStyle(color: Colors.black,fontSize: 13), ),
              SizedBox(height: 5,),
              Divider(
                color: Colors.grey,
              )
            ],
           ),
        );
      },
    );
  }
}