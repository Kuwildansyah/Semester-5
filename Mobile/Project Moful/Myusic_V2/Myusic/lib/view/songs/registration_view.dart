import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:music_player/common/color_extension.dart';
import 'package:music_player/view_model/registration_view_model.dart';

class RegistrationView extends StatelessWidget {
  final vm = Get.put(RegistrationViewModel());

  RegistrationView({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            TextField(
              controller: vm.txtEmail.value,
              decoration: InputDecoration(
                  prefixIcon: Container(
                    alignment: Alignment.centerLeft,
                    width: 30,
                    child: const Icon(Icons.email),
                  ),
                  hintText: "Email",
                  hintStyle: TextStyle(
                    color: TColor.primaryText28,
                    fontSize: 13,
                  )),
            ),
            TextField(
              controller: vm.txtPwd.value,
              // obscureText: true,
              decoration: InputDecoration(
                  prefixIcon: Container(
                    alignment: Alignment.centerLeft,
                    width: 30,
                    child: const Icon(Icons.key),
                  ),
                  hintText: "Password",
                  hintStyle: TextStyle(
                    color: TColor.primaryText28,
                    fontSize: 13,
                  )),
            ),
            ElevatedButton(
              onPressed: () {
                vm.register();
              },
              child: const Text("Register"),
            )
          ],
        ),
      ),
    );
  }
}
