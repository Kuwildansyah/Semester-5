<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Item extends Model
{
    use HasFactory;
    protected $table = 'item'; // Sesuaikan dengan nama tabel di database
    protected $fillable = ['name','created_at','updated_at']; // Kolom yang dapat diisi
}
