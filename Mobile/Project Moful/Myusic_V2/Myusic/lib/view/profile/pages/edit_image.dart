import 'dart:io' as io;

import 'package:appwrite/appwrite.dart';
import 'package:appwrite/models.dart';
import 'package:flutter/material.dart';
import 'package:music_player/data/appwrite.dart';
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

  final client = AppWriteClient.getInstance();
  Storage? storage;
  Databases? databases;
  Document? about;

  @override
  void initState() {
    super.initState();
    storage = Storage(client);
    databases = Databases(client);

    getUserAbout();
  }

  void updateImage(String images) {
    user.image = images;
  }

  void getUserAbout() async {
    about = await databases?.listDocuments(
        databaseId: '656d8c83cc211f925bed',
        collectionId: '656d8c9023ac97f70691',
        queries: [
          Query.equal("userId", "65646536b64bac7a0c67")
        ]).then((value) => value.documents.first);

    if (about != null) {
      final location = await getApplicationDocumentsDirectory();

      final by = await storage?.getFileView(
          bucketId: "656da092a070e11fb10c", fileId: about?.data["picture"]);

      final imagefile = io.File('${location.path}/pict.png');
      imagefile.writeAsBytesSync(by!);
      user.image = imagefile.path;
    }
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

                      final up = await storage?.createFile(
                          bucketId: "656da092a070e11fb10c",
                          fileId: ID.unique(),
                          file: InputFile.fromPath(path: image.path));

                      if (about != null) {
                        final docID = about?.$id;
                        final upd = await databases?.updateDocument(
                            databaseId: '656d8c83cc211f925bed',
                            collectionId: '656d8c9023ac97f70691',
                            documentId: docID!,
                            data: {"picture": up?.$id});
                      }

                      final name = basename(image.path);
                      final imageFile = io.File('${location.path}/$name');
                      final newImage =
                          await io.File(image.path).copy(imageFile.path);
                      setState(() => user =
                          user.copy(imagePath: newImage.path.toString()));
                    },
                    child: user.image.startsWith('http')
                        ? Image.network(user.image)
                        : Image.file(io.File(user.image)),
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
