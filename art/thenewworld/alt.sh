for x in *jpg
do

echo $x
bordereffects -s 10 -d 5 -c 25 -g 5 -p 10 -b white $x alt/$x

done
