#!/bin/bash

printf "Input : "
read semester

declare -a IPS Mahasiswa

i=0 
let banyak=$semester-1

while [ $i -le $banyak ];
do 
        let nilai=$i+1
        printf "semester %.i: " $nilai;
        read nilaisemester;
        IPSMahasiswa[$i]=$nilaisemester;
        let jumlah=jumlah+$nilaisemester;
        let i=$i+1

done

let IPK=$jumlah/$semester
echo "IPS mahasiswa = " $jumlah "/" $semester 
echo "IPK mahasiswa = $IPK"
