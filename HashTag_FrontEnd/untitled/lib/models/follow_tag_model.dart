import 'dart:convert';

class Follows_Tag {
  String? followingtag;
  String? followerUser;
 

  Follows_Tag({
    this.followingtag,
    this.followerUser,
    
  });

  factory Follows_Tag.fromJson(Map<String, dynamic> json) {
    return Follows_Tag(
      followingtag: json['followingtag'],
      followerUser: json['followerUser'],
      
    );
  }
}