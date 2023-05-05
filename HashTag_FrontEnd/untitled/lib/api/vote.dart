import 'dart:async';
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:untitled/api/post_api.dart';
import 'package:untitled/constant.dart';
import 'package:untitled/models/post_model.dart';
import 'package:tuple/tuple.dart';
// class PostData
// {
//   int? upvote_count;
//   int? downvote_count;

//   PostData({
//     this.upvote_count,
//     this.downvote_count,
//   });
// }
//  Future<int> likePost(String post_id) async {
//     var token = await getToken();
//     bool is_liked = false;
//     var response =
//         await http.post(Uri.parse('$baseUrl/post/upvote/$post_id'), headers: {
//       'Authorization': 'Token $token',
//     });
//     if(response.statusCode==200)
//     {
//       print('Post upvoted successfully');

//     // Get updated post data to retrieve new upvote count
//     var postResponse = await http.get(
//       Uri.parse('$baseUrl/post/detail/$post_id'),
//       headers: {'Authorization': 'Token $token'},
//     );

//     if (postResponse.statusCode == 200) {
//       Map<String, dynamic> postData = jsonDecode(postResponse.body);
//       int upvote_count = postData['upvote_count'];

//       // Return the updated upvote count
//       return upvote_count;
//     } else {
//       // Failed to retrieve updated post data
//       throw Exception('Failed to retrieve updated post data');
//     }
//     }
//     else{
//       throw Exception('Failed to upvote post');
//     }

//   }

// Future<Post> likePost(String post_id) async {
//   var token = await getToken();
//   bool is_liked = false;
//   var response = await http.post(Uri.parse('$baseUrl/post/upvote/$post_id'), headers: {
//     'Authorization': 'Token $token',
//   });
//   if (response.statusCode == 200) {
//     print('Post upvoted successfully');

//     // Get updated post data to retrieve new upvote count
//     var postResponse = await http.get(
//       Uri.parse('$baseUrl/post/detail/$post_id'),
//       headers: {'Authorization': 'Token $token'},
//     );

//     if (postResponse.statusCode == 200) {
//       Map<String, dynamic> postData = jsonDecode(postResponse.body);
//       int upvote_count = postData['upvote_count']??0;
//       int downvote_count = postData['downvote_count']??0;

//       // Update the value of upvote_count
      
//       Post postdata = Post(upvote_count: upvote_count, downvote_count: downvote_count);
//       // Return the updated upvote count
//       return postdata;
      
//     } else {
//       // Failed to retrieve updated post data
//       throw Exception('Failed to retrieve updated post data');
//     }
//   } else {
//     throw Exception('Failed to upvote post');
//   }
// }
Future<Tuple2<int, int>> likePost(String post_id) async {
  var token = await getToken();

  var response = await http.post(Uri.parse('$baseUrl/post/upvote/$post_id'), headers: {
    'Authorization': 'Token $token',
  });
  if (response.statusCode == 200) {
    print('Post upvoted successfully');

    // Get updated post data to retrieve new upvote count
    var postResponse = await http.get(
      Uri.parse('$baseUrl/post/detail/$post_id'),
      headers: {'Authorization': 'Token $token'},
    );

    if (postResponse.statusCode == 200) {
      Map<String, dynamic> postData = jsonDecode(postResponse.body);
      int upvoteCount = postData['upvote_count']??0;
      int downvoteCount = postData['downvote_count']??0;
    
      // Return the updated upvote count
      return Tuple2<int, int>(upvoteCount, downvoteCount);
      
    } else {
      // Failed to retrieve updated post data
      throw Exception('Failed to retrieve updated post data');
    }
  } else {
    throw Exception('Failed to upvote post');
  }
}
  Future<Tuple2<int, int>> unlikePost(String post_id) async {
    var token = await getToken();
    var response = await http.post(
      Uri.parse('$baseUrl/post/downvote/$post_id'),
      headers: {
        'Authorization': 'Token $token',
      },
    );
    if (response.statusCode == 200) {
    print('Post upvoted successfully');

    // Get updated post data to retrieve new upvote count
    var postResponse = await http.get(
      Uri.parse('$baseUrl/post/detail/$post_id'),
      headers: {'Authorization': 'Token $token'},
    );

    if (postResponse.statusCode == 200) {
      Map<String, dynamic> postData = jsonDecode(postResponse.body);
      int upvoteCount = postData['upvote_count']??0;
      int downvoteCount = postData['downvote_count']??0;
      
      // Return the updated upvote count
      return Tuple2<int, int>(upvoteCount, downvoteCount);
      
    } else {
      // Failed to retrieve updated post data
      throw Exception('Failed to retrieve updated post data');
    }
  } else {
    throw Exception('Failed to downvote post');
  }
}