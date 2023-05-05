import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:untitled/api/auth/auth_api.dart';

import '../models/user_cubit.dart';
import '../models/user_models.dart';
import 'home.dart';

class SignUp extends StatefulWidget {
  const SignUp({Key? key}) : super(key: key);

  @override
  State<SignUp> createState() => _SignUpState();
}

class _SignUpState extends State<SignUp> {
  TextEditingController emailController =  TextEditingController();
  TextEditingController usernameController =  TextEditingController();
  TextEditingController passwordController =  TextEditingController();
  TextEditingController confirmController =  TextEditingController();
  @override
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
                      keyboardType: TextInputType.emailAddress,
                      style: TextStyle(color: Colors.black),
                      controller: emailController,
                      decoration: InputDecoration(
                          fillColor: Colors.grey.shade100,
                          filled: true,
                          hintText: "Email",
                          prefixIcon: Icon(Icons.mail,color:Colors.black),

                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(20),
                          )),
                    ),
                    SizedBox(
                      height: 10,
                    ),
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
                      height: 10,
                    ),
                    TextField(
                      controller: confirmController,
                      obscureText: true,
                      style: TextStyle(color: Colors.black),
                      decoration: InputDecoration(
                          fillColor: Colors.grey.shade100,
                          filled: true,
                          hintText: "Confirm Password",
                          prefixIcon: Icon(Icons.lock,color:Colors.black),
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(20),
                          )),
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
                        onPressed: ()async{
                          var authRes= await registerUser(usernameController.value.text, emailController.value.text, passwordController.value.text, confirmController.value.text);
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
                            return Homepage();
                          },

                          
                            ),

                            );
                        };
                        // child: Text('SIGNUP', style: TextStyle(color: Colors.black),
                        
                        },
                        child: Text("SIGNUP",style: TextStyle(color: Colors.white)),
                      ),
                    
                    ),
                    SizedBox(
                      height: 10,
                    ),
                    // Column(
                    //   children:[
                    //     Text('or',style: TextStyle(fontSize: 12),),
                    //     SizedBox(
                    //       height: 8,
                    //     ),
                    //     Text('Continue with Google'),
                    //     SizedBox(
                    //       height: 8,
                    //     ),
                    //     Text('Continue with Facebook'),
                    //     ///Add google and facebook picture before text
                    //   ],
                    // ),
                    SizedBox(
                      height: 20,
                    ),
                    Row(
                      children: [

                        Text("Have an Account?"),

                        SizedBox(
                          width: 60,
                        ),

                        Container(
                          child:TextButton(

                            onPressed: (){
                              Navigator.pushNamed(context, 'login');
                            },
                            child: Text('Login here', style: TextStyle(
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
