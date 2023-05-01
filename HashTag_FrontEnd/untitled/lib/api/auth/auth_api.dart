import "dart:convert";

import "package:hive_flutter/hive_flutter.dart";
import "package:http/http.dart" as http;
import "package:untitled/constant.dart";

import '../../models/user_models.dart';

var authtoken;
Future<dynamic> userAuth(String username, String password) async{
  Map body = 
  {
    "username": username,
    // "email": "",
    "password": password,
  };
  
  var url = Uri.parse("$baseUrl/user/auth/login/");
  var res = await http.post(url, body: body);
  authtoken = res.body;
  print(res.body);
  print(res.statusCode);
  if(res.statusCode==200)
  {
    Map json = jsonDecode(res.body);
    String token = json['key'];
    var box =await Hive.openBox(tokenBox);
    box.put("token",token);
    authtoken =box.get('token');
    User? user = await getUser(token);
    // putTokenValue(token);
    
    return user;
  }
  else 
  {
    Map json = jsonDecode(res.body);
    if(json.containsKey("username"))
    {
      return json["email"][0];
    }
    if(json.containsKey("pasword"))
    {
      return json["password"][0];
    }
     if(json.containsKey("non_field_errors"))
    {
      return json["non_field_errors"][0];
    }
  }
}

Future<User?>? getUser(String token)
async {
  var url = Uri.parse("$baseUrl/user/auth/user/");
  var res = await http.get(
    url,
    headers: {
      'Authorization':'Token ${token}',
    }
  );
  if(res.statusCode == 200)
  {
    var json = jsonDecode(res.body);
    User user =  User.fromJSon(json);
    user.token = token;
    return user;
    
  }
  else
  {
    return null;
  }
  
}

Future<dynamic>? registerUser(
  String username,
  String email,
  String password,
  String confirm_password,
  )
async {
  Map<String,dynamic> data = {
    "username": username,
    "email": email,
    "password1": password,
    "password2": confirm_password,
};
  var url = Uri.parse("$baseUrl/user/auth/registration/");
  var res = await http.post(
    url,
    body: data,
  );
  if(res.statusCode == 200 || res.statusCode == 201)
  {
    Map json = jsonDecode(res.body);
    if(json.containsKey("key"))
    {
      String token = json["key"];
      var box = await Hive.openBox(tokenBox);
      box.put("token",token);
      var a = await getUser(token);
      if(a!= null)
     {
        User user = a;
        return user;
      }
      else{
       return null;
      }
    }
    else if(res.statusCode ==  400)
    {
        Map json = jsonDecode(res.body);
        if(json.containsKey("email"))
      {
        return json["email"][0];
      }
      else if(json.containsKey("password"))
      {
        return json["password"][0];
      }
    }
    
    
    
  }
  else
  {
    print(res.body);
    print(res.statusCode);
    return null;
  }
  
}
Future<User?>? logout(String token)
async {
  var url = Uri.parse("$baseUrl/user/auth/logout/");
  var res = await http.get(
    url,
    headers: {
      'Authorization':'Token ${token}',
    }
  );
 
}

