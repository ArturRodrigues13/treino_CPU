for i in {1..10}; do
	echo visitando binga $i
	python boi.py < input/boi$i | diff - output/boi$i --strip-trailing-cr
done
