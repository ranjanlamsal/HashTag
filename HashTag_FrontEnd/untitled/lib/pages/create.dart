import 'package:flutter/material.dart';



class Create extends StatefulWidget {
  const Create({Key? key}) : super(key: key);

  @override
  State<Create> createState() => _CreateState();
}

class _CreateState extends State<Create> {
  @override
  Widget build(BuildContext context) {


    return Scaffold(
      backgroundColor: Color.fromARGB(255, 243, 244, 255),
      appBar: AppBar(
        leading: IconButton(
          icon: Icon(Icons.arrow_back),
          color: Colors.black,
          onPressed: (){
            Navigator.pushNamed(context, 'home');
          },
        ),
        backgroundColor:Color.fromARGB(255, 243, 244, 255),
        elevation: 1,
        // title: Image.asset("assets/logo.png",
        // width : 100,
        // ),
        // alignment: Alignment.topLeft,
        centerTitle: false,

        bottom: PreferredSize(
          preferredSize: Size(20,20),

          child: Column(

            children: [


              Text('Create Post',
                style: TextStyle(
                    color: Colors.indigoAccent,fontSize: 20,fontWeight: FontWeight.w700
                ),
              ),


            ],
          ),

        ),


      ),
      body: ListView(
        children: [
          SizedBox(
            height: 400,
            width: double.infinity,
            child:TextField(
              expands: true,
           maxLines: null,
              decoration: InputDecoration(
                hintText: "What's On your Mind?"
              ),
            )
          ),
          SizedBox(
            height: 70,
          ),
          Padding(
            padding: const EdgeInsets.only(left: 20, right:200),
            child: Container(
              width: double.infinity,
              child: RawMaterialButton(
                fillColor: Color.fromARGB(255, 83,84,176),
                padding: EdgeInsets.symmetric(vertical: 15.0),
                shape:  RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(12)
                ),
                onPressed: (){

                },
                child: Text('Generate Tag', style: TextStyle(color: Colors.white,),
                ),
              ),
            ),
          ),
        ],


      )





    );
  }
}
