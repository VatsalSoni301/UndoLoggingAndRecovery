a=0
b=1
for var in "$@"
do
    a=`expr $a + $b`
done

if [ $a == 2 ]
then
	python2 2018201005_1.py $1 $2
else
	python2 2018201005_2.py $1
fi