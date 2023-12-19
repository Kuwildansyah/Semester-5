<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Form</title>
</head>
<body>

    <h2>Login</h2>
    
    <form id="loginForm">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>

        <button type="button" onclick="login()">Login</button>
    </form>

    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script>
        function login() {
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            axios.post('http://127.0.0.1:8000/login', {
                email: email,
                password: password
            })
            .then(function (response) {
                const accessToken = response.data.access_token;
                console.log('Login success! Access Token:', accessToken);
            })
            .catch(function (error) {
                console.error('Login failed!', error.response.data);
            });
        }
    </script>
</body>
</html>
