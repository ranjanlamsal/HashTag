import 'dart:async';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:untitled/api/auth/auth_api.dart';
import 'package:untitled/api/post_api.dart';
import "package:untitled/constant.dart";
import 'package:untitled/models/follow_tag_model.dart';
import 'package:untitled/models/post_model.dart';
import 'package:untitled/models/user_models.dart';
import 'package:hive_flutter/hive_flutter.dart';

import '../models/tag_model.dart';

Future<String?> getToken() async {
  var box = await Hive.openBox(tokenBox);
  var token = box.get("token") as String?;
  return token;
} 

List<Post> self_tags=[];
Future<List<Tag>> getSelf_tag() async {
  print("Done");
  var token = await getToken();
  var response = await http
      .get(Uri.parse('$baseUrl/tag/self/'),
      headers: {
        // 'Authorization': 'Token $token',
            'Authorization': 'Token $token',
  },      );
  var data = jsonDecode(response.body.toString());
  print(data);
  if (response.statusCode == 200) {
    List<dynamic> data = jsonDecode(response.body);
    print(response.body);
    List<Tag> self_tags = data.map((postJson) => Tag.fromJson(postJson)).toList();
    return self_tags;
  } else {
    throw Exception('Failed to load tags');
  }
}

List<Post> tag_postlist=[];

Future<List<Post>> getTag_Post(String tag_name) async {

  var token = await getToken();
  var response = await http
      .get(Uri.parse('$baseUrl/post/list/$tag_name'),
      headers: {
        // 'Authorization': 'Token $token',
            'Authorization': 'Token $token',
  },      );
  var data = jsonDecode(response.body.toString());
  print(data);
  if (response.statusCode == 200) {
    List<dynamic> data = jsonDecode(response.body);
    print(response.body);
    List<Post> tag_post = data.map((postJson) => Post.fromJson(postJson)).toList();
    return tag_post;
  } else {
    throw Exception('Failed to load tags');
  }
}

Future followTag(String tagName) async{
  var token = await getToken();
  var response = await http
      .post(Uri.parse('$baseUrl/tag/followtag/$tagName'),
      headers: {
        // 'Authorization': 'Token $token',
            'Authorization': 'Token $token',
  },      );
 
  if(response.statusCode == 200)
  {
    print("Unfollowed Tag sucessfully");
  }
  else if(response.statusCode ==201)
  {
    print("Followed Tag Sucessfully");
  }
  else 
  {
    throw Exception("Failed");
  }
}

Future<List<Follows_Tag>> getTagFollowers(String tagName)async
{
    var token = await getToken();
  var response = await http
      .post(Uri.parse('$baseUrl/tag/followers/$tagName'),
      headers: {
        // 'Authorization': 'Token $token',
            'Authorization': 'Token $token',
  },      );
  var data = jsonDecode(response.body.toString());
  print(data);
  if(response.statusCode == 200)
  {
    List<dynamic> data = jsonDecode(response.body);
    print(response.body);
    List<Follows_Tag> followers = data.map((postJson) => Follows_Tag.fromJson(postJson)).toList();
    return followers;
  }
  
  else 
  {
    throw Exception("Failed");
  }
}


Future<List> getTotalPostTag() async {
  var token = await getToken();
  var response = await http
      .get(Uri.parse('$baseUrl/post/totalposttag/'),
      headers: {
        // 'Authorization': 'Token $token',
            'Authorization': 'Token $token',
  },      );
  if (response.statusCode == 200) {
    List<dynamic> data = jsonDecode(response.body);
    return data;
  } else {
    throw Exception('Failed to load tags');
  }
}




