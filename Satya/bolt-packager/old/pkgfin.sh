#! /bin/bash
tar_url=$1
version=$2
echo "Version Aquired: ${version}"
sleep 0.5s
mkdir SOURCES
cd SOURCES
wget ${tar_url}
cd .. 
mkdir SPECS
text=$(echo ${version} | tr -d "v")
cp .specs/example.spec SPECS/numix-theme.spec
lineNumber=$(grep -n -m 1 "Version" SPECS/numix-theme.spec | cut -f1 -d:)
echo ${lineNumber}
sed -i "${lineNumber}s/.*/Version:        ${text}/g" SPECS/numix-theme.spec
