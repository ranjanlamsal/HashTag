import 'package:flutter/material.dart';
import 'package:untitled/pages/create.dart';
import 'package:untitled/pages/home.dart';
import 'package:untitled/pages/profile.dart';
import 'package:untitled/pages/recomended.dart';
import 'package:untitled/pages/trending.dart';

class StartPage extends StatefulWidget {
  StartPage({Key? key}) : super(key: key);

  @override
  State<StartPage> createState() => _StartPageState();
}

class _StartPageState extends State<StartPage> {
  int currentTab = 0;
  final List<Widget> screens =[
    Homepage(),
    Create(),
    Profile(),
    Recommended(),
    Trending(),
    Create()

    
  ];
  final PageStorageBucket bucket = PageStorageBucket();
  Widget currentScreen = Profile();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
     body: PageStorage(
        child: currentScreen,
        bucket: bucket,
      ),
      // floatingActionButton: FloatingActionButton(
      //   backgroundColor: Colors.indigoAccent,
      //   child: Icon(Icons.add),

      //   onPressed: () {
      //     Navigator.pushNamed(context, 'Create');
      //   },
      // ),
      floatingActionButtonLocation: FloatingActionButtonLocation.centerDocked,
      bottomNavigationBar: BottomAppBar(
        shape: CircularNotchedRectangle(),
        color:Color.fromARGB(255, 202,207,250), 
        notchMargin: 10,
        child: Container(
          height:60,
          child:Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              MaterialButton(
                  minWidth: 30,
                  onPressed:(){
                    setState(() {
                      currentScreen=Homepage();
                      currentTab=0;
                    });
                  },
                  child:Column(
              mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Icon(
                        Icons.home,
                        color: Colors.indigoAccent,
                      ),
                      // Text('Home',
                      //   style: TextStyle(color:Colors.indigoAccent,),
                      // )
                    ],
          )
              ),
              MaterialButton(
                  minWidth: 30,
                  onPressed:(){
                    setState(() {
                      currentScreen=Trending();
                      currentTab=1;
                    });
                  },
                  child:Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Icon(
                        Icons.trending_up_rounded,
                        color:Colors.indigoAccent,
                      ),
                      // Text('Trending',
                      //   style: TextStyle(color:  Colors.indigoAccent ,),
                      // )
                    ],
                  )
              ),
              MaterialButton(
                  minWidth: 30,
                  onPressed:(){
                    setState(() {
                      currentScreen=Create();
                      currentTab=1;
                    });
                  },
                  child:Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Icon(
                        Icons.add_circle,
                        color:Colors.indigoAccent,
                      ),
                      // Text('Create',
                      //   style: TextStyle(color:  Colors.indigoAccent ,),
                      // )
                    ],
                  )
              ),

                
              
              MaterialButton(
              minWidth: 30,
              onPressed:(){
                setState(() {
                  currentScreen=Recommended();
                  currentTab=3;
                });
              },
              child:Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Icon(
                    Icons.recommend,
                    color: Colors.indigoAccent,
                  ),
                  // Text('Recommended',
                  //   style: TextStyle(color:Colors.indigoAccent,),
                  // )
                ],
              )
              ),
              MaterialButton(
              minWidth: 30,
              onPressed:(){
                setState(() {
                  currentScreen=Profile();
                  currentTab=4;
                });
              },
              child:Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Icon(
                    Icons.person,
                    color:Colors.indigoAccent,
                  ),
                  // Text('Profile',
                  //   style: TextStyle(color:  Colors.indigoAccent ,),
                  // )
                ],
              )
              )
          ])
        ),
      ),
    );
  }
}
