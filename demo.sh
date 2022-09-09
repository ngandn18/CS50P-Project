# bash shell
for test in t1 t2 t3 t4 t5 f1 f2
do
echo "###"
echo "### Test with input file $test"
cat $test | python project.py | tee result.$test
echo "### End test with input file $test"
done

echo "***"
echo "List of result files"
ls -l result.*
