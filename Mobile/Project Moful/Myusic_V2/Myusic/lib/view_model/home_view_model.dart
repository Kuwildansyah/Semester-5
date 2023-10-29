import 'package:dio/dio.dart';
import 'package:flutter/widgets.dart';
import 'package:get/get.dart';
import 'package:music_player/data/api/api_service.dart';
import 'package:music_player/model/spotify_popular_playlist.dart';

class HomeViewModel extends GetxController {
  final txtSearch = TextEditingController().obs;

  @override
  void onInit() {
    super.onInit();
    fetchPlaylist();
  }

  final hostRecommendedArr = [
    {
      "image": "assets/img/img_1.png",
      "name": "Sound of Sky",
      "artists": "Dilon Bruce"
    },
    {
      "image": "assets/img/img_2.png",
      "name": "Girl on Fire",
      "artists": "Alecia Keys"
    }
  ].obs;

  final RxList<PlaylistItem> playListArr = <PlaylistItem>[].obs;

  final recentlyPlayedArr = [
    {"rate": 4, "name": "Billie Jean", "artists": "Michael Jackson"},
    {"rate": 4, "name": "Earth Song", "artists": "Michael Jackson"},
    {"rate": 4, "name": "Mirror", "artists": "Justin Timberlake"},
    {"rate": 4, "name": "Remember the Time", "artists": "Michael Jackson"}
  ].obs;

  fetchPlaylist() async {
    try {
      var response = await dio.get(Endpoints.featuredPlaylist,
          options: Options(headers: {
            "authorization":
                "Bearer BQDZzp3cqOQoETuS-UP475Vkb0hK6WOU3iI7DR6LQ3YJNSVbNiMpuGbZsA9zzSy52JQodOCYgoLulLctNh2s3SMsOgsv3GIdvCBnAY_IXHmLOlrcQT4"
          }));
      var data = PopularPlaylist.fromJson(response.data["playlists"]);
      playListArr.addAll(data.items);
      update();
    } catch (e) {
      print(e);
    }
  }
}

//.navigationViewStyle(StackNavigationViewStyle())
