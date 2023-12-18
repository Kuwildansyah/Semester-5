import 'package:get/get.dart';
import 'package:appwrite/appwrite.dart';

class appwrite extends GetxController {
  Client client = Client();
  @override
  void onInit() {
    super.onInit();
    // appwrite
    const endPoint = " https://cloud.appwrite.io/v1";
    const projectID = "656463377fb602dc46c6";
    client
        .setEndpoint(endPoint)
        .setProject(projectID)
        .setSelfSigned(status: true);
  }
}
