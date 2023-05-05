import 'dart:convert';

class Reply {
  int? id;
  int? commentId;
  String? replied_by;
  DateTime? reply_time;
  String? reply;
  

  Reply({
    this.id,
    this.commentId,
    this.replied_by,
    this.reply_time,
    this.reply,
  });

  factory Reply.fromJson(Map<String, dynamic> json) {
    return Reply(
      id: json['id'],
      commentId: json['commentId'],
      replied_by: json['replied_by'],
      reply_time: DateTime.parse(json['reply_time']),
      reply: json['reply'],
    );
  }
}