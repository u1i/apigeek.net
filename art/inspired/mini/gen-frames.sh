mkdir -p tmp framed

frame[0]="1"
frame[1]="2"
frame[2]="4"
frame[3]="6"
frame[4]="8"

for x in *jpg
do
	echo $x
	rand=$[ $RANDOM % 5 ]

	picframe -f ${frame[$rand]} -m 40 -b 1 $x tmp/$x
	convert tmp/$x -geometry 200x200! framed/$x
done
