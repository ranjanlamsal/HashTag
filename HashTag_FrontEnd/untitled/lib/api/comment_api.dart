import "dart:convert";
import "dart:async";
import 'package:http/http.dart' as http;
import "package:untitled/api/post_api.dart";
import "package:untitled/constant.dart";
import "package:untitled/models/comment_model.dart";

import "../models/reply_model.dart";

Future<List<Comment>> getComment(String postid) async {
  var token = await getToken();
  var response = await http.get(Uri.parse("$baseUrl/post/comment/$postid"),
  headers: {
    'Authorization': 'Token $token',
  });
  var data = jsonDecode(response.body);

  print(data);
  print(data.runtimeType);
  if(response.statusCode == 200)
  {
    List<dynamic> data = jsonDecode(response.body);
    print(response.body);
    List<Comment> comment = data.map((postJson) =>Comment.fromJson(postJson)).toList();
    return comment;
  }
  else {
    throw Exception('Failed to load Comments');
  }
}
Future<String> getCommentCount(String postid) async {
  var token = await getToken();
  var response = await http.get(
    Uri.parse("$baseUrl/post/comment/$postid"),
    headers: {
      'Authorization': 'Token $token',
    },
  );
  var data = jsonDecode(response.body);

  print(data);
  print(data.runtimeType);
  if (response.statusCode == 200) {
    List<dynamic> commentsData = jsonDecode(response.body);
    print(response.body);
    List<Comment> comments = commentsData.map((commentJson) => Comment.fromJson(commentJson)).toList();
    return comments.length.toString();
  } else {
    throw Exception('Failed to load Comments');
  }
}
Future<List<Reply>> getReply(String commentid) async {
  var token = await getToken();
  var response = await http.get(Uri.parse("$baseUrl/post/reply/$commentid"),
  headers: {
    'Authorization': 'Token $token',
  });
  var data = json.decode(response.body);
if (data is List<dynamic>) {
  List<Reply> replies = data.map((replyJson) => Reply.fromJson(replyJson)).toList();
  return replies;
} else if (data is Map<String, dynamic>) {
  Reply reply = Reply.fromJson(data);
  return [reply]; // Wrap single reply in a list
} else {
  throw Exception('Invalid response format');
}
  // var data = json.decode(response.body);
  //   print(data);
  //   print(data.runtimeType);
  //   print(response.statusCode);
  //   if (response.statusCode == 200) 
  //   {
   
  //   List<dynamic> data = jsonDecode(response.body);
  //   print(response.body);
  //   List<Reply> replies = data.map((replyJson) => Reply.fromJson(replyJson)).toList();
   
  //   return replies;
  //   } 
  //   else {
  //   throw Exception('Failed to load Replies');
  // }
}


//   if(response.statusCode == 200) {
//     dynamic data = jsonDecode(response.body);
//     if (data is List) {
//       List<Reply> replies = data.map((postJson) =>Reply.fromJson(postJson)).toList();
//       return replies;
//     } else if (data is Map<String, dynamic>) {
//       List<Reply> replies = [];
//       data.forEach((key, value) {
//         if (value is List) {
//           List<Reply> replyList = value.map((postJson) =>Reply.fromJson(postJson)).toList();
//           replies.addAll(replyList);
//         }
//       });
//       return replies;
//     }
//   } else {
//     throw Exception('Failed to load Replies');
//   }
// }

Future<dynamic>? addComment(
  
  String postId,
  String commentor_by,
  
  String comment,
  
)
async {
  var token = await getToken();
  Map<String,dynamic> data = 
  {
    "postId": postId,
    "commentor_by": commentor_by,
    "comment_time": DateTime.now().toString(),
    "comment": comment,
  };
  var url = Uri.parse("$baseUrl/post/comment/$postId");
  var res = await http.post(
    url,
    body: data,
    headers: {
      'Authorization':'Token ${token}',
    }
  );
   if(res.statusCode == 200 || res.statusCode == 201)
   {
    Map json = jsonDecode(res.body);
    print(res.body);
   }
}



