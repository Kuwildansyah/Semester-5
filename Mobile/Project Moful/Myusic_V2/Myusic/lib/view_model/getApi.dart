
class GetApi {
int userId;
int id;
String title;
String body;
GetApi({
required this.userId,
required this.id,
required this.title,
required this.body,
});
factory GetApi.fromJson(Map<String, dynamic> json) => GetApi(
userId: json["userId"],
id: json["id"],
title: json["title"],
body: json["body"],);
Map<String, dynamic> toJson() => {
"userId": userId,
"id": id,
"title": title,
"body": body,
};
}