import 'dart:convert';

class Post {
  int? id;
  String? content;
  String?  posted_by_user;
  DateTime? created_at;
  String? tag_name;
  int? upvote_count;
  int? downvote_count;

  Post({
    this.id,
    this.content,
    this.posted_by_user,
    this.created_at,
    this.tag_name,
    this.upvote_count,
    this.downvote_count,
  });

  factory Post.fromJson(Map<String, dynamic> json) {
    return Post(
      id: json['id'],
      content: json['content'],
      posted_by_user: json['posted_by_user'],
      created_at: DateTime.parse(json['created_at']),
      tag_name: json['tag_name'],
      upvote_count: json['upvote_count'],
      downvote_count: json['downvote_count'],
    );
  }
}