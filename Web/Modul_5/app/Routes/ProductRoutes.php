<?php

namespace app\Routes;

include "app/Controller/ProductController.php";

use app\Controller\ProductController;

class ProductRoutes{
    public function handle($method, $path){
        
        if ($method == 'GET' && $path == '/api/product'){
            $controller = new ProductController();
            echo $controller->index();
        }

        
        if ($method == 'GET' && strpos($path, '/api/product') == 0){
        
            $pathParts = explode('/', $path);
            $id = $pathParts[count($pathParts) - 1];

            $controller = new ProductController();
            echo $controller->getById($id);
        }

        
        if ($method == 'POST' && $path == '/api/product'){
            $controller = new ProductController();
            echo $controller->insert();
        }

        
        if ($method == 'PUT' && strpos($path, '/api/product') == 0){
        
            $pathParts = explode('/', $path);
            $id = $pathParts[count($pathParts) - 1];

            $controller = new ProductController();
            echo $controller->update($id);
        }

        
        if ($method == 'DELETE' && strpos($path, '/api/product') == 0){
            $pathParts = explode('/', $path);
            $id = $pathParts[count($pathParts) - 1];

            $controller = new ProductController();
            echo $controller->delete($id);
        }

        
        if ($method == 'GET' && $path == '/api/products-with-categories') {
            $controller = new ProductController();
            echo $controller->indexWithCategory();
        }
        
        
        if ($method == 'GET' && strpos($path, '/api/products-by-category') == 0) {
            $pathParts = explode('/', $path);
            $category_id = $pathParts[count($pathParts) - 1];

            $controller = new ProductController();
            echo $controller->findByCategoryId($category_id);
        }

        
        if ($method == 'PUT' && strpos($path, '/api/add-category-to-product') == 0) {
        
            $pathParts = explode('/', $path);
            $id = $pathParts[count($pathParts) - 2];
            $category_id = $pathParts[count($pathParts) - 1];

            $controller = new ProductController();
            echo $controller->addCategory($id, $category_id);
        }
        
        
        if ($method == 'GET' && strpos($path, '/api/products-by-sold') == 0) {
            $pathParts = explode('/', $path);
            $sold_id = $pathParts[count($pathParts) - 1];

            $controller = new ProductController();
            echo $controller->getSoldProducts($sold_id);
        }
    }


}