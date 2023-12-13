

import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:music_player/view/home/home_view.dart';
import 'package:music_player/view/home/screen.dart';
// import 'package:music_player/view/main_tabview/main_tabview.dart';
import 'package:music_player/view/home/welcome_page.dart';
import 'package:music_player/view/profile/pages/profile_page.dart';

class SplashViewMode extends GetxController {

    var scaffoldKey = GlobalKey<ScaffoldState>();

    void loadView() async {
       await Future.delayed(const Duration(seconds: 2) );
       Get.to( () =>  WelcomePage() );
    }

    void openDrawer(){
        scaffoldKey.currentState?.openDrawer();
    }

    void closeDrawer(){
        scaffoldKey.currentState?.closeDrawer();
    }
}