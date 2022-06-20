filename=$1

for commit in $(git rev-list HEAD)

do

timestamp=$(git show -s --format=%ci $commit | cut -d' ' -f1)

content=$(git show $commit:$filename)

echo "$content" > "/tmp/$filename.$timestamp"

done


files=$(ls -1 /tmp/$filename.* | sort -n)

last=""

for file in $files

do

content=$(cat $file)

if [ "$content" = "$last" ]

then

rm $file

else

last=$content

fi

done
