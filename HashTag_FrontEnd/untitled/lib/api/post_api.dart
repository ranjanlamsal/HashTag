import 'dart:async';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:untitled/api/auth/auth_api.dart';
import "package:untitled/constant.dart";
import 'package:untitled/models/post_model.dart';
import 'package:untitled/models/user_models.dart';
import 'package:hive_flutter/hive_flutter.dart';

// Future<String?> getToken() async {
//   await Hive.openBox('tokenBox'); // Open the Hive box

//   final box = Hive.box('tokenBox'); // Get a reference to the box
//   final token = box.get('token');
//   print(token) // Get the token value from the box

//   return token; // Return the token value (which may be null)
// }

Future<String?> getToken() async {
  var box = await Hive.openBox(tokenBox);
  var token = box.get("token") as String?;
  return token;
} 

List<Post> postList =[];
List<Post> selfpostList =[];
Future<List<Post>> getPost() async {
  var token = await getToken();
  var response = await http
      .get(Uri.parse('$baseUrl/post/list/'),
      headers: {
        // 'Authorization': 'Token $token',
    'Authorization': 'Token $token',
  },      );
  var data = jsonDecode(response.body.toString());
  // print(data);
  if (response.statusCode == 200) {
    List<dynamic> data = jsonDecode(response.body);
    print(response.body);
    List<Post> posts = data.map((postJson) => Post.fromJson(postJson)).toList();
    return posts;
  } else {
    throw Exception('Failed to load posts');
  }
}



Future<List<Post>> getSelfPost() async {
  var token = await getToken();
  var response = await http
      .get(Uri.parse('$baseUrl/post/self/'),
      headers: {
        // 'Authorization': 'Token $token',
    'Authorization': 'Token $token',
  },      );
  var data = jsonDecode(response.body.toString());
  // print(data);
  if (response.statusCode == 200) {
    List<dynamic> data = jsonDecode(response.body);
    print(response.body);
    List<Post> selfposts = data.map((postJson) => Post.fromJson(postJson)).toList();
    return selfposts;
  } else {
    throw Exception('Failed to load posts');
  }
}
