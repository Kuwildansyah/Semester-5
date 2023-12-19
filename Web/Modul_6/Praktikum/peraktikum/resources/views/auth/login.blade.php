<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Form</title>
</head>
<body>

    <form class="login" id="loginForm">
        <input type="text" id="username" placeholder="Username">
        <input type="password" id="password" placeholder="Password">
        <button type="button" onclick="login()">Login</button>
    </form>

    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script>
        function login() {
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            axios.post('http://127.0.0.1:8000/login', {
                email: username, // assuming username is the email
                password: password
            })
            .then(function (response) {
                const accessToken = response.data.access_token;
                // Simpan access token sesuai kebutuhan (localStorage, cookie, dll.)
                console.log('Login success! Access Token:', accessToken);
            })
            .catch(function (error) {
                console.error('Login failed!', error.response.data);
            });
        }
    </script>
</body>
</html>
