import 'dart:convert';

class Tag {
  int? id;
  String? content;
  String? created_by;
  DateTime? created_at;
  String? title;

  Tag({
    this.id,
    this.content,
    this.created_by,
    this.created_at,
    this.title,
  });

  factory Tag.fromJson(Map<String, dynamic> json) {
    return Tag(
      id: json['id'],
      content: json['content'],
      created_by: json['created_by'],
      created_at: DateTime.parse(json['created_at']),
      title: json['title'],
    );
  }
}