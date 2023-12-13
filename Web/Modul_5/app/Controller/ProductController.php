<?php

namespace app\Controller;

include "app/Traits/ApiResponseFormatter.php";
include "app/Models/Product.php";

use app\Models\Product;
use app\Traits\ApiResponseFormatter;

class ProductController{
    use ApiResponseFormatter;

    public function index(){
        $productModel = new Product();
        $response = $productModel->findAll();
        return $this->apiResponse(200, "Success", $response);

    }


    public function getById($id){
        $productModel = new Product();
        $response = $productModel->findById($id);
        return $this->apiResponse(200, "Success", $response);
    }


    public function insert(){
        $jsonInput = file_get_contents('php://input');
        $inputData = json_decode($jsonInput, true);
        if (json_last_error()){
            return $this->apiResponse(400, "Error invalid input", null);
        }

        $productModel = new Product();
        $response = $productModel->create([
            "product_name" => $inputData['product_name']
        ]);
        
        return $this->apiResponse(200, "Success", $response);
    }


    public function update($id){
       
        $jsonInput = file_get_contents('php://input');
        $inputData = json_decode($jsonInput, true);
       
        if (json_last_error()){
            return $this->apiResponse(400, "Error invalid input", null);
        }

        $productModel = new Product();
        $response = $productModel->update([
            "product_name" => $inputData['product_name']
        ], $id);
        
        return $this->apiResponse(200, "Success", $response);
    }


    public function delete($id){
        $productModel = new Product();
        $response = $productModel->destroy($id);
        
        return $this->apiResponse(200, "Success", $response);
    }

    //cari semua dari category
    public function indexWithCategory()
    {
        $productModel = new Product();
        $response = $productModel->findAllWithCategory();
        return $this->apiResponse(200, "Success", $response);
    }

    public function findByCategoryId($category_id)
    {
        $productModel = new Product();
        $response = $productModel->findByCategoryId($category_id);

        if (empty($response)) {
            return $this->apiResponse(404, "No products found for the given category_id", null);
        }

        return $this->apiResponse(200, "Success", $response);
    }

    public function addCategory($id, $category_id)
    {
        $productModel = new Product();
        $productModel->addCategoryId($id, $category_id);

        return $this->apiResponse(200, "Success: Category added to product", null);
    }
    public function getSoldProducts($isSold)
{
    $productModel = new Product();
    $response = $productModel->findSoldProducts($isSold);
    return $this->apiResponse(200, "Success", $response);
}

    
}