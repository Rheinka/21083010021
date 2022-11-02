#!/bin/bash

panjang() {
    echo "Masukkan panjang: "
    read panjang
}

lebar() {
     echo "Masukkan lebar: "
     read lebar
}

luas() {
    let hasil=$panjang*$lebar 
    echo -e  "Luas persegi panjang : \n$hasil "
}

panjang
lebar
luas
