import 'package:dio/dio.dart';

BaseOptions dioOptions = BaseOptions(
    baseUrl: "https://api.spotify.com/v1", responseType: ResponseType.json);

final Dio dio = Dio(dioOptions);

class Endpoints {
  static var featuredPlaylist = "/browse/featured-playlists";
}
