import 'package:dio/dio.dart';
import 'package:music_player/data/api/api_service.dart' as api_service;
import 'package:music_player/view_model/home_view_model.dart';
import 'package:test/test.dart';
import 'package:mockito/mockito.dart';
import 'package:http_mock_adapter/http_mock_adapter.dart';

class MockDio extends Mock implements Dio {}

void main() {
  group('fetchPlaylist', () {
    test('should fetch and update playlist', () async {
      // Arrange
      final dio = api_service.dio;
      final dioAdapter = DioAdapter(dio: dio);
      dio.httpClientAdapter = dioAdapter;

      final homeViewModel = HomeViewModel();

      // Mocking the Dio response using http_mock_adapter
      dioAdapter.onGet(
          api_service.Endpoints.featuredPlaylist,
          (server) => server.reply(200, {
                "playlists": {
                  "href":
                      "https://api.spotify.com/v1/me/shows?offset=0&limit=20",
                  "limit": 20,
                  "next":
                      "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
                  "offset": 0,
                  "previous":
                      "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
                  "total": 4,
                  "items": [
                    {
                      "collaborative": false,
                      "description": "string",
                      "external_urls": {"spotify": "string"},
                      "href": "string",
                      "id": "string",
                      "images": [
                        {
                          "url":
                              "https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228",
                          "height": 300,
                          "width": 300
                        }
                      ],
                      "name": "string",
                      "owner": {
                        "external_urls": {"spotify": "string"},
                        "followers": {"href": "string", "total": 0},
                        "href": "string",
                        "id": "string",
                        "type": "user",
                        "uri": "string",
                        "display_name": "string"
                      },
                      "public": false,
                      "snapshot_id": "string",
                      "tracks": {"href": "string", "total": 0},
                      "type": "string",
                      "uri": "string"
                    }
                  ]
                }
              }));

      // Act
      await homeViewModel.fetchPlaylist();

      // Assert
      // Add your assertions here, for example:
      expect(homeViewModel.playListArr, isNotEmpty);
    });

    // test('should handle error gracefully', () async {
    //   // Arrange
    //   final dio = Dio(BaseOptions());
    //   final dioAdapter = DioAdapter();
    //   dio.httpClientAdapter = dioAdapter;

    //   final yourClass = YourClass(dio);

    //   // Mocking the Dio response to simulate an error
    //   dioAdapter.onGet(Endpoints.featuredPlaylist).reply(404, {});

    //   // Act
    //   await yourClass.fetchPlaylist();

    //   // Assert
    //   // Add your assertions here, for example:
    //   expect(yourClass.playListArr, isEmpty);
    //   verifyNever(yourClass.update());
    // });
  });
}
