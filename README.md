# Best Practices
## Description

This repository demonstrates coding best practices. 
The program `get_column_stats.py` takes arguments of
`--filename` and `--column_number` and returns the mean 
and standard deviation of the specified row. The 
program `style.py` is a template for formatting to PEP8 
standards.

## Usage

To run `get_column_stats.py` have Python 3.6 installed 
and perform the following:
```
python get_column_stats.py --filename [file_name] --column_number [column_number]
```

Where `[file_name]` is the name of the file of interest, and `[column_number]`
is the column of that file for which you would like the mean and standard deviation. 

## Testing

To use prebuilt functional tests on the style and functionality of `style.py` and
`get_column_stats.py` perform the following:
``` 
bash basics_test.sh
```
All functional tests should be passed. 

## Installation

The only major installation required is `pycodestyle`. In your conda environment, run
the following:
```
conda install pycodestyle
```

