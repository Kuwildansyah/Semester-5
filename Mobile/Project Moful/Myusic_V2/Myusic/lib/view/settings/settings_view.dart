import 'package:flutter/material.dart';
// import 'package:flutter_webview_pro/webview_flutter.dart';
import 'package:get/get.dart';
import 'package:music_player/common_widget/icon_text_row.dart';
import 'package:music_player/view/songs/registration_view.dart';
import 'package:music_player/view_model/splash_view_model.dart';
import 'package:music_player/view/profile/pages/profile_page.dart';

import '../../common/color_extension.dart';

class SettingsView extends StatefulWidget {
  const SettingsView({super.key});

  @override
  State<SettingsView> createState() => _SettingsViewState();
}

class _SettingsViewState extends State<SettingsView> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: TColor.bg,
        elevation: 0,
        leading: IconButton(
          onPressed: () {
            Get.find<SplashViewMode>().openDrawer();
          },
          icon: Image.asset(
            "assets/img/menu.png",
            width: 25,
            height: 25,
            fit: BoxFit.contain,
          ),
        ),
        title: Text(
          "Settings",
          style: TextStyle(
              color: TColor.primaryText80,
              fontSize: 17,
              fontWeight: FontWeight.w600),
        ),
      ),
      body: Column(
        // Wrap your ListView with a Column
        children: [
          Expanded(
            // Make the ListView expand to take available space
            child: ListView(
              children: [
                IconTextRow(
                  title: "User",
                  icon: "assets/img/app_logo.png",
                  onTap: () {
                    Get.to(() => RegistrationView());
                  },
                ),
                IconTextRow(
                  title: "Display",
                  icon: "assets/img/s_display.png",
                  onTap: () {},
                ),
                IconTextRow(
                  title: "Audio",
                  icon: "assets/img/s_audio.png",
                  onTap: () {},
                ),
                IconTextRow(
                  title: "Headset",
                  icon: "assets/img/s_headset.png",
                  onTap: () {},
                ),
                IconTextRow(
                  title: "Lock Screen",
                  icon: "assets/img/s_lock_screen.png",
                  onTap: () {},
                ),
                IconTextRow(
                  title: "Advanced",
                  icon: "assets/img/s_menu.png",
                  onTap: () {},
                ),
                IconTextRow(
                  title: "Other",
                  icon: "assets/img/s_other.png",
                  onTap: () {},
                ),
                IconTextRow(
                  title: "Profile",
                  icon:
                      "assets/img/userwhite.png", // Replace with your desired icon
                  onTap: () {
                    // Use GetX to navigate to the WebView page
                    Get.to(() => const ProfilePage());
                  },
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
