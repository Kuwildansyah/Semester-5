

import 'package:flutter/material.dart';
import 'package:get/get.dart';
// import 'package:music_player/view/main_tabview/main_tabview.dart';
import 'package:music_player/view/home/signin_page.dart';

class SplashViewMode extends GetxController {

    var scaffoldKey = GlobalKey<ScaffoldState>();

    void loadView() async {
       await Future.delayed(const Duration(seconds: 2) );
       Get.to( () => SignInPage() );
    }

    void openDrawer(){
        scaffoldKey.currentState?.openDrawer();
    }

    void closeDrawer(){
        scaffoldKey.currentState?.closeDrawer();
    }
}