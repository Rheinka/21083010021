#!/bin/bash

distroLinuxDesktop[0]=BlankOn
distroLinuxDesktop[1]=Ubuntu
distroLinuxDesktop[2]=Debian
distroLinuxDesktop[3]=ArchLinux
distroLinuxDesktop[4]=LinuxMint

distroLinuxDesktop[0]=UbuntuServer
distroLinuxDesktop[1]=CentOS
distroLinuxDesktop[2]=FedoraServer

#cara mengambil milai array
echo ${distroLinuxDesktop[*]}
echo ${distroLinuxServer[*]}
