#!/bin/bash
file="input.txt"
y=0
pwr=1
ans=0
x=0
md=$(( 10**9 + 7))
for line in $(cat $file)
do
if [ $y -eq 0 ]
then
 x=$line
 y=1
else
 ans=$(( $ans+$line*$pwr ))
 ans=$(( $ans % $md))
 pwr=$(( $pwr*$x ))
 pwr=$(( $pwr % $md ))
fi
done
echo $ans > ./output.txt
