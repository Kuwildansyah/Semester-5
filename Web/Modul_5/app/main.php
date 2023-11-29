<?php 
header("Content-Type: application/json; charset=UTF-8");

include "Routes/Product_Routes.php";

use app\Routes\ProductRoutes;

// TANGKAP REQUEST METHOD 
$method = $_SERVER['REQUEST_METHOD'];
// TANGKAP REQUEST PATH
$path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

// PANGGIL ROUTES
$productRoute = new ProductRoutes();
$productRoute -> handle($method, $path);