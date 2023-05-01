import 'package:flutter/material.dart';


 class Trending extends StatefulWidget {
   const Trending({Key? key}) : super(key: key);

   @override
   State<Trending> createState() => _TrendingState();
 }

 class _TrendingState extends State<Trending> {
   @override
   Widget build(BuildContext context) {


    return Scaffold(
      backgroundColor: Color.fromARGB(255, 243,244,255),
      appBar: AppBar(

        leading: IconButton(
          icon: Icon(Icons.arrow_back),
          color: Colors.black,
          onPressed: (){
            Navigator.pushNamed(context, 'home');
          },
        ),
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
           SizedBox(
         height:10,
            )
            ],
          ),

        ),

      ),


   body: Container(

     child: ListView(
       children: [
         SizedBox(
           height: 10,
         ),
         Text('  #World Cup',
           style: TextStyle(
               color: Colors.black,fontSize: 20,fontWeight: FontWeight.w500
           ),
         ),
         SizedBox(
           height:10,
         ),
         Text('     1000 Updates             550 Posts',
           style: TextStyle(
             color: Colors.black,fontSize: 10,
           ),
         ),
         // Row(
         //   children: [
         //     Text('1000 Updates',
         //       style: TextStyle(
         //         color: Colors.black,fontSize: 8,
         //       ),
         //     ),
         //     Text('550 Posts',
         //       style: TextStyle(
         //         color: Colors.black,fontSize: 8,
         //       ),
         //     ),
         //   ],
         // ),

         SizedBox(
           height:70,
         ),
         Text('  #EarthQuake',
           style: TextStyle(
             color: Colors.black,fontSize: 20,fontWeight: FontWeight.w500
           ),
         ),
         SizedBox(
           height:10,
         ),
         Text('     1000 Updates             550 Posts',
           style: TextStyle(
             color: Colors.black,fontSize: 10,
           ),
         ),



         SizedBox(
           height:70,
         ),
         Text('  #BitCoin',
           style: TextStyle(
               color: Colors.black,fontSize: 20,fontWeight: FontWeight.w500
           ),
         ),
         SizedBox(
           height:10,
         ),
         Text('     1000 Updates             550 Posts',
           style: TextStyle(
             color: Colors.black,fontSize: 10,
           ),
         ),

         SizedBox(
           height:70,
         ),
         Text('  #Education',
           style: TextStyle(
               color: Colors.black,fontSize: 20,fontWeight: FontWeight.w500
           ),
         ),
         SizedBox(
           height:10,
         ),
         Text('     1000 Updates             550 Posts',
           style: TextStyle(
             color: Colors.black,fontSize: 10,
           ),
         ),

         SizedBox(
           height:70,
         ),
         Text('  #BasketBall',
           style: TextStyle(
               color: Colors.black,fontSize: 20,fontWeight: FontWeight.w500
           ),
         ),
         SizedBox(
           height:10,
         ),
         Text('     1000 Updates             550 Posts',
           style: TextStyle(
             color: Colors.black,fontSize: 10,
           ),
         ),
         SizedBox(
           height:70,
         ),
         Text('   #World',
           style: TextStyle(
               color: Colors.black,fontSize: 20,fontWeight: FontWeight.w500
           ),
         ),
         SizedBox(
           height:10,
         ),
         Text('     1000 Updates             550 Posts',
           style: TextStyle(
             color: Colors.black,fontSize: 10,
           ),
         ),

       ],
     ),
   ),




    );

   }

}
