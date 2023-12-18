import 'package:appwrite/appwrite.dart';
import 'package:appwrite/models.dart';
import 'package:flutter/material.dart';
import 'package:music_player/data/appwrite.dart';
import '../user/user_data.dart';
import '../widgets/appbar_widget.dart';

// This class handles the Page to edit the About Me Section of the User Profile.
class EditDescriptionFormPage extends StatefulWidget {
  const EditDescriptionFormPage({super.key});

  @override
  _EditDescriptionFormPageState createState() =>
      _EditDescriptionFormPageState();
}

class _EditDescriptionFormPageState extends State<EditDescriptionFormPage> {
  final _formKey = GlobalKey<FormState>();
  final descriptionController = TextEditingController();
  var user = UserData.myUser;

  final client = AppWriteClient.getInstance();
  Databases? databases;
  Document? about;

  @override
  void initState() {
    super.initState();

    databases = Databases(client);
    getUserAbout();
  }

  void getUserAbout() async {
    about = await databases?.listDocuments(
        databaseId: '656d8c83cc211f925bed',
        collectionId: '656d8c9023ac97f70691',
        queries: [
          Query.equal("userId", "65646536b64bac7a0c67")
        ]).then((value) => value.documents.first);

    descriptionController.text = about?.data["about"];
  }

  @override
  void dispose() {
    descriptionController.dispose();
    super.dispose();
  }

  void updateUserValue(String description) async {
    user.aboutMeDescription = description;

    if (about == null) {
      Document? result = await databases?.createDocument(
        databaseId: '656d8c83cc211f925bed',
        collectionId: '656d8c9023ac97f70691',
        documentId: ID.unique(),
        data: {
          "userId": "65646536b64bac7a0c67",
          "about": description,
        },
      );
    } else {
      final docID = about?.$id;
      final result = await databases?.updateDocument(
          databaseId: '656d8c83cc211f925bed',
          collectionId: '656d8c9023ac97f70691',
          documentId: docID!,
          data: {
            "userId": "65646536b64bac7a0c67",
            "about": description,
          });
    }
  }

  void delete() async {
    if (about != null) {
      final docID = about?.$id;
      print(docID);
      final result = await databases?.deleteDocument(
        databaseId: '656d8c83cc211f925bed',
        collectionId: '656d8c9023ac97f70691',
        documentId: docID!,
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: buildAppBar(context),
        body: Form(
          key: _formKey,
          child: Column(
              crossAxisAlignment: CrossAxisAlignment.center,
              mainAxisAlignment: MainAxisAlignment.start,
              children: <Widget>[
                const SizedBox(
                    width: 350,
                    child: Text(
                      "What type of passenger\nare you?",
                      style:
                          TextStyle(fontSize: 25, fontWeight: FontWeight.bold),
                    )),
                Padding(
                    padding: const EdgeInsets.all(20),
                    child: SizedBox(
                        height: 250,
                        width: 350,
                        child: TextFormField(
                          // Handles Form Validation
                          validator: (value) {
                            if (value == null ||
                                value.isEmpty ||
                                value.length > 200) {
                              return 'Please describe yourself but keep it under 200 characters.';
                            }
                            return null;
                          },
                          controller: descriptionController,
                          textAlignVertical: TextAlignVertical.top,
                          decoration: const InputDecoration(
                              alignLabelWithHint: true,
                              contentPadding:
                                  EdgeInsets.fromLTRB(10, 15, 10, 100),
                              hintMaxLines: 3,
                              hintText:
                                  'Write a little bit about yourself. Do you like chatting? Are you a smoker? Do you bring pets with you? Etc.'),
                        ))),
                Padding(
                    padding: const EdgeInsets.only(top: 50),
                    child: Align(
                        alignment: Alignment.bottomCenter,
                        child: SizedBox(
                          width: 350,
                          height: 50,
                          child: ElevatedButton(
                            onPressed: () {
                              // Validate returns true if the form is valid, or false otherwise.
                              if (_formKey.currentState!.validate()) {
                                updateUserValue(descriptionController.text);
                                Navigator.pop(context);
                              }
                            },
                            child: const Text(
                              'Update',
                              style: TextStyle(fontSize: 15),
                            ),
                          ),
                        ))),
                Padding(
                    padding: const EdgeInsets.only(top: 50),
                    child: Align(
                        alignment: Alignment.bottomCenter,
                        child: SizedBox(
                          width: 350,
                          height: 50,
                          child: ElevatedButton(
                            onPressed: () async {
                              // Validate returns true if the form is valid, or false otherwise.
                              if (_formKey.currentState!.validate()) {
                                delete();
                                Navigator.pop(context);
                              }
                            },
                            child: const Text(
                              'Delete',
                              style: TextStyle(fontSize: 15),
                            ),
                          ),
                        )))
              ]),
        ));
  }
}
