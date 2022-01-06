for x in *jpg
do

convert $x -crop 945x1515+75+175 +repage out/$x

done
