import 'package:appwrite/appwrite.dart';

class AppWriteClient {
  static Client? _instance;

  static Client getInstance() {
    _instance ??= Client()
          .setEndpoint('https://appwrite.mnizarzr.dev/v1')
          .setProject('65645063320d837afe95')
          .setSelfSigned(status: true);

    return _instance!;
  }
}
