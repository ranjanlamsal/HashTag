import 'dart:convert';
class User{
  int? id;
  String? token;
  String? username;
  String? email,first_name,last_name;


  User({
    this.email,
    this.first_name,
    this.last_name,
    this.id,
    this.username,

  });

  factory User.fromJSon(json){
    return User(
      email: json["email"],
      first_name: json["first_name"],
      id: json["id"],
      last_name: json["last_name"],
      username: json["username"],
    );

  }

}
