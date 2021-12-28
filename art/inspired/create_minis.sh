mkdir -p mini
rm mini/*jpg

for x in *jpg
do
	echo $x
	convert $x -crop 945x945+0+100 -geometry 100x100 +repage mini/$x
done
