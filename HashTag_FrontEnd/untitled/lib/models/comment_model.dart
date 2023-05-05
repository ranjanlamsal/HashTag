import 'dart:convert';

class Comment {
  int? id;
  int? postId;
  String?  commentor_by;
  DateTime? comment_time;
  String? comment;
  

  Comment({
    this.id,
    this.postId,
    this.commentor_by,
    this.comment_time,
    this.comment,
  });

  factory Comment.fromJson(Map<String, dynamic> json) {
    return Comment(
      id: json['id'],
      postId: json['postId'],
      commentor_by: json['commentor_by'],
      comment_time: DateTime.parse(json['comment_time']),
      comment: json['comment'],
    );
  }
}