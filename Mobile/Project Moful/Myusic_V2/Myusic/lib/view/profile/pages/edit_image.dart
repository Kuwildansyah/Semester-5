import 'dart:io';

import 'package:flutter/material.dart';
import '../user/user_data.dart';
import 'package:path_provider/path_provider.dart';
import 'package:path/path.dart';
import '../widgets/appbar_widget.dart';
import 'package:image_picker/image_picker.dart';

class EditImagePage extends StatefulWidget {
  const EditImagePage({super.key});

  @override
  _EditImagePageState createState() => _EditImagePageState();
}

class _EditImagePageState extends State<EditImagePage> {
  var user = UserData.myUser;

 void updateImage(String images ){
    user.image = images ;
  }
  
// void updateImage(String image) async {
//   try {
//     final location = await getApplicationDocumentsDirectory();
//     final name = basename(image.path);
//     final imageFile = File('${location.path}/$name');
//     final newImage = await image.copy(imageFile.path);

//     setState(() => user = user.copy(imagePath: newImage.path));
//   } catch (e) {
//     print('Error updating image: $e');
//   }
// }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: buildAppBar(context),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        mainAxisAlignment: MainAxisAlignment.start,
        children: <Widget>[
          const SizedBox(
              width: 330,
              child: Text(
                "Upload a photo of yourself:",
                style: TextStyle(
                  fontSize: 23,
                  fontWeight: FontWeight.bold,
                ),
              )),
          Padding(
              padding: const EdgeInsets.only(top: 20),
              child: SizedBox(
                  width: 330,
                  child: GestureDetector(
                    onTap: () async {
                      final image = await ImagePicker()
                          .pickImage(source: ImageSource.gallery);

                      if (image == null) return;

                      final location = await getApplicationDocumentsDirectory();
                      final name = basename(image.path);
                      final imageFile = File('${location.path}/$name'); 
                      final newImage =
                          await File(image.path).copy(imageFile.path);
                      setState(
                          () => user = user.copy(imagePath: newImage.path.toString()));
                    },
                    child: user.image.startsWith('http')
                          ? Image.network(user.image)
                           : Image.file(File(user.image)),
          
                  ))),
          Padding(
              padding: const EdgeInsets.only(top: 40),
              child: Align(
                  alignment: Alignment.bottomCenter,
                  child: SizedBox(
                    width: 330,
                    height: 50,
                    child: ElevatedButton(
                      onPressed: () {
                     updateImage(user.image);
                        
                          Navigator.pop(context);
                       },
                      child: const Text(
                        'Update',
                        style: TextStyle(fontSize: 15),
                      ),
                    ),
                  )))
        ],
      ),
    );
  }
}