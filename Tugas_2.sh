#!/bin/bash

echo "========DAFTAR MENU========"
echo "1. Pizza (50000)"
echo "2. Burger (34000)"
echo "3. Coca Cola (10000)"
echo "4. Ayam Krispi (20000)"
echo "==========================="

read -p "Masukkan Pilihan Menu Anda: " pil;

if [ $pil -eq 1 ]; 
then
   echo "Beli berapa porsi?";

read jum1

let bayar=jum1*50000

elif [ $pil -eq 2 ]; 
then
   echo "Beli berapa porsi?";

read jum2

let bayar=jum2*34000

elif [ $pil -eq 3 ]; 
then
   echo "Beli berapa porsi?";

read jum3

let bayar=jum3*10000

elif [ $pil -eq 4 ]; 
then
   echo "Beli berapa porsi?"; 

read jum4

let bayar=jum4*20000
else
   echo "Maaf menu yang anda pilih tidak tersedia";
fi
   echo "Uang yang harus anda bayarkan: Rp.$bayar"

