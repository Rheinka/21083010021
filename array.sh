#!/bin/bash

distroLinux=("Mint" "Ubuntu" "Kali" "Arch" "Debian")

let pilih=$RANDOM%5

echo "Saya Memilih Distro $pilih, ${distroLinux[$pilih]} !"

