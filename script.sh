#!/bin/bash -x

while read -r line;
do
   echo "$line" ;
   $line ;
done < pytest.file
