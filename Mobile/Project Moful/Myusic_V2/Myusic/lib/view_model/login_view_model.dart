import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';

class LoginViewModel extends GetxController {
  final txtEmail = TextEditingController().obs;
  final txtPwd = TextEditingController().obs;

  final auth = FirebaseAuth.instance;
  User? user;

  login() async {
    try {
      final credential = await auth.signInWithEmailAndPassword(
        email: txtEmail.value.text,
        password: txtPwd.value.text,
      );
      user = credential.user;
    } on FirebaseAuthException catch (e) {
      if (e.code == 'user-not-found') {
        print('No user found for that email.');
      } else if (e.code == 'wrong-password') {
        print('Wrong password provided for that user.');
      }
    }
  }
}
