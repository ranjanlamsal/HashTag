

import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:hive/hive.dart';
import 'package:untitled/api/auth/auth_api.dart';
import 'package:untitled/constant.dart';
import 'package:untitled/models/user_cubit.dart';
import 'package:untitled/models/user_models.dart';
import 'package:untitled/pages/home.dart';
import 'package:untitled/pages/login.dart';
import 'package:untitled/pages/signup.dart';
import 'package:hive_flutter/hive_flutter.dart';
import 'package:untitled/pages/start_page.dart';
void main() async{
  WidgetsFlutterBinding.ensureInitialized();
  
  await Hive.initFlutter();
  runApp(MyApp());
}
class MyApp extends StatelessWidget 
{
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return BlocProvider(
      create:(context){
        return UserCubit(User());
      } ,
      child: MaterialApp(
        debugShowCheckedModeBanner: false,
        title: 'Flutter',
        home: FutureBuilder<Box> (
          future: Hive.openBox(tokenBox),
          builder: (context,snapshot)
          {
            if(snapshot.hasData)
            {
              var box = snapshot.data;
              var token = box!.get("token");

              if(token!=null) 
              {
                  return FutureBuilder<User?>
                  (
                    future: getUser(token),
                    builder: (context,snapshot)
                  {
                    if(snapshot.hasData)
                    {
                      if(snapshot.hasData != null)
                      {
                        User user = snapshot.data!;
                        user.token = token;
                        context.read<UserCubit>().emit(user);
                        return  StartPage();
                      }
                      else
                      {
                        return const MyLogin();
                      }
                      
                    }
                    else
                    {
                      return const MyLogin();
                    }
                 }
                 );
              } else{
               return const MyLogin();
            }
            
          } else if(snapshot.hasError)
          {
            return const MyLogin();
          }
  
        
        
        
          
            
            else 
            {
              return const MyLogin();
            }     
          }
          ),
          ),
      
    );
  }
}





