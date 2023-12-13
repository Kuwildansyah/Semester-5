import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:music_player/home/view/signin_page.dart';

void main() {
  testWidgets('SignInPage UI Test', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(
      MaterialApp(
        home: SignInPage(),
      ),
    );

    // Verify if the widgets are rendered correctly.

    // Verify the existence of the "Welcome back." text.
    expect(find.text('Welcome back.'), findsOneWidget);

    // Verify the existence of the "You've been missed!" text.
    expect(find.text("You've been missed!"), findsOneWidget);

    // Verify the existence of the text field with the hint text.
    expect(find.widgetWithText(TextField, 'Phone, email or username'), findsOneWidget);

    // Verify the existence of the "Don't have an account?" text.
    expect(find.text("Don't have an account? "), findsOneWidget);

    // Verify the existence of the "Register" text.
    expect(find.text('Register'), findsOneWidget);

    // Verify the existence of the "Sign In" button.
    expect(find.text('Sign In'), findsOneWidget);

    // Verify the existence of the back arrow button.
    expect(find.byType(IconButton), findsOneWidget);

    // You can add more tests based on your UI requirements.
  });

  // You can add more test cases as needed.
}
