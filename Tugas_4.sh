#!/bin/bash

read -p "Input: " input;
 
for ((angka=$input; angka>=1; angka=angka-2))
do
  echo $angka
done

