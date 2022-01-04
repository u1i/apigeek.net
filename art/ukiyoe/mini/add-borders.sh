for x in *jpg
do
	echo $x
	convert $x -bordercolor black  -border 5x5 tmp/$x
done
