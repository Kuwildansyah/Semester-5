import 'package:appwrite/appwrite.dart';
import 'package:appwrite/models.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:music_player/data/appwrite.dart';

class LoginAWViewModel extends GetxController {
  final txtEmail = TextEditingController().obs;
  final txtPwd = TextEditingController().obs;

  final client = AppWriteClient.getInstance();
  final user = Rxn<User>();

  login() async {
    try {
      final account = Account(client);

      await account.createEmailSession(
        email: txtEmail.value.text,
        password: txtPwd.value.text,
      );

      user.value = await account.get();
    } on Exception catch (e) {
      print(e);
    }
  }
}
