#!/bin/bash
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest
 
# Test for PEP8 style on style.py and get_column_stats.py
run test_pep8_style pycodestyle style.py
assert_exit_code 0
assert_no_stdout

run test_pep8_get_column_stats pycodestyle get_column_stats.py
assert_exit_code 0
assert_no_stdout

# Test for that random values of mean and stdev converge at (16XXX) and (94XX)
(for i in `seq 1 100000`; do
    echo -e "$RANDOM";
done )> data.txt

run test_mean_stdev python get_column_stats.py --filename data.txt --column_number 0

assert_exit_code 0
assert_in_stdout 'mean: 16'
assert_in_stdout 'stdev: 94' 
assert_stdout
assert_no_stderr

# Test case for 10 rows of values 0 to 10; makes sure mean = value and stdev = 0
for ((i=1;i<=10;i++));
do
    echo -e "0\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10";
done > data.txt

for ((i=0;i<=10;i++));
do
    mean="'mean: $i'"
    run test_zero_behavior python get_column_stats.py --filename data.txt --column_number $i
    assert_exit_code 0
    assert_in_stdout mean
    assert_in_stdout 'stdev: 0'
    assert_stdout
    assert_no_stderr
done

# Test for errors
run test_no_inputs python get_column_stats.py
assert_no_stdout
assert_in_stderr 'arguments are required'
assert_exit_code 2

run test_no_file python get_column_stats.py --filename fakefile.txt --column_number 0
assert_no_stdout
assert_in_stderr 'Could not find fakefile.txt'
assert_exit_code 1

run test_no_column python get_column_stats.py --filename data.txt --column_number 100
assert_no_stdout
assert_in_stderr 'Column 100 not in range'
assert_exit_code 1

for ((i=1;i<=10;i++));
do
    echo -e "a\tb\tc";
done > letters.txt

run test_letters python get_column_stats.py --filename letters.txt --column_number 0
assert_no_stdout
assert_in_stderr 'Non-integer value in letters.txt'
assert_exit_code 1

chmod -rwx data.txt

run test_permissions python get_column_stats.py --filename data.txt --column_number 0
assert_no_stdout
assert_in_stderr 'Could not open data.txt due to permissions'
assert_exit_code 1

chmod +rwx data.txt
rm data.txt
rm letters.txt
