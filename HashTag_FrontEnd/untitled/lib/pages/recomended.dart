import 'package:flutter/material.dart';

class Recommended extends StatefulWidget {
  const Recommended({Key? key}) : super(key: key);

  @override
  State<Recommended> createState() => _RecommendedState();
}

class _RecommendedState extends State<Recommended> {
  @override
  Widget build(BuildContext context) {


    return Scaffold(
        backgroundColor: Color.fromARGB(255, 202, 207, 250),
        appBar: AppBar(
          backgroundColor: Color.fromARGB(255, 202, 207, 250),
          elevation: 0,
          title: Image.asset("assets/logo.png",
            width: 70,
          ),
          // alignment: Alignment.topLeft,
          centerTitle: false,
          actions: [
            IconButton(
                onPressed: () {},
                icon: Icon(Icons.search),
                color: Colors.black),
            IconButton(onPressed: () {},
                icon: Icon(Icons.notifications_active_outlined),
                color: Colors.indigoAccent),

          ],


          bottom: PreferredSize(
            preferredSize: Size(20,20),
            child: Column(


              children: [


                Text('Recommended For You',
                  style: TextStyle(
                      color: Colors.black,fontSize: 20,fontWeight: FontWeight.w700
                  ),
                ),
                SizedBox(
                  height:10 ,
                )

              ],
            ),

          ),
        ),
       


    );
  }
  }
