import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:http/http.dart' as http;
import 'package:untitled/api/auth/auth_api.dart';
import 'package:untitled/models/user_cubit.dart';
import 'package:untitled/models/user_models.dart';
import 'package:untitled/pages/signup.dart';
import 'package:untitled/pages/start_page.dart';
import 'home.dart';


class MyLogin extends StatefulWidget {
  const MyLogin({Key? key}) : super(key: key);

  @override
  State<MyLogin> createState() => _MyLoginState();
}

class _MyLoginState extends State<MyLogin> {
  
  TextEditingController usernameController = TextEditingController();
  TextEditingController passwordController = TextEditingController();
  TextEditingController emailController = TextEditingController();
  
  @override
  bool isChecked=false;
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        image: DecorationImage(
          image: AssetImage('assets/background.png')
        ),
      ),
      child: Scaffold(
        backgroundColor: Colors.transparent,
        body: Stack(
          children: [
            SingleChildScrollView(
              child: Container(
                padding: EdgeInsets.only(top: MediaQuery.of(context).size.height*0.42,
                right: 65,
                  left: 65,
                ),
                child : Column(
                  children: [
                    TextField(
                      controller: usernameController,
                      style: TextStyle(color: Colors.black),
                      decoration: InputDecoration(
                          fillColor: Colors.grey.shade100,
                          filled: true,
                          hintText: "Username",
                          prefixIcon: Icon(Icons.account_circle,color:Colors.black),
                
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(20),
                          )),
                    ),
                    SizedBox(
                      height: 10,
                    ),
                    TextField(
                      controller: passwordController,
                      obscureText: true,
                      style: TextStyle(color: Colors.black),
                      decoration: InputDecoration(
                          fillColor: Colors.grey.shade100,
                          filled: true,
                          hintText: "Password",
                          prefixIcon: Icon(Icons.lock,color:Colors.black),
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(20),
                          )),
                    ),
                    SizedBox(
                     height: 8,
                    ),
                    Row(
                      children: [
                
                     Checkbox(value: isChecked, onChanged: (value){
                       isChecked=! isChecked;
                       setState(() {
                
                       });
                     }
                     ),
                        Text('Remember me',style: TextStyle(fontSize: 12),),
                
                        SizedBox(
                          width: 45,
                        ),
                        Text('Forgot Password',style: TextStyle(fontSize: 10,decoration: TextDecoration.underline),),
                      ],
                    ),
                    SizedBox(
                      height: 20,
                    ),
                    Container(
                      width: double.infinity,
                      child: RawMaterialButton(
                        fillColor: Color.fromARGB(255, 83,84,176),
                       padding: EdgeInsets.symmetric(vertical: 15.0),
                        shape:  RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(12)
                        ),
                        onPressed: () async{
                          var authRes = await userAuth(usernameController.text, passwordController.text);
                          if(authRes.runtimeType == String)
                          {
                            showDialog(context: context,
                             builder: (context){
                              return Dialog(
                                child: Container(alignment:Alignment.center,
                                height: 200,
                                width: 250,
                                decoration: BoxDecoration(),
                                child: Text(authRes),),
                              );
                             });
                          }
                          else if(authRes.runtimeType==User){
                            User user = authRes;
                            context.read<UserCubit>().emit(user);
                            Navigator.of(context).push(MaterialPageRoute(builder: (context){
                            return StartPage();
                          }
                          )
                          );

                          }
                          
                        },
                        child: Text('LOGIN', style: TextStyle(color: Colors.white),),
                      ),
                    ),
                    SizedBox(
                      height: 20,
                    ),
                    // Row(
                    //   children:[
                    //   Text('Login with'),
                    //     ///Add facebook and all like figma
                    //  ],
                    // ),
                    SizedBox(
                      height: 20,
                    ),
                    Row(
                      children: [
                
                        Text("Don't have a accout?"),
                
                        SizedBox(
                          width: 30,
                        ),
                
                        Container(
                            child:TextButton(
                
                              onPressed: (){
                                Navigator.of(context).push(MaterialPageRoute(builder: (context){
                                  return SignUp();
                                }
                                )
                                );

                              },
                              child: Text('Register Here', style: TextStyle(
                                decoration: TextDecoration.underline,
                                  color: Colors.black),
                              ),
                            ),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
            )
          ],

        ),

      ),

    );


  }
}
