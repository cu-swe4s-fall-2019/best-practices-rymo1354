import sys
import argparse
import math


def parse_arguments():

    parser = argparse.ArgumentParser(description='Mean and standard deviation \
                                     of given column from given text file',
                                     prog='the_good_way')
    parser.add_argument('--filename',
                        type=str,
                        help='Name of file',
                        required=True)
    parser.add_argument('--column_number',
                        type=int,
                        help='Column number',
                        required=True)
    args = parser.parse_args()

    return args


def get_column_from_file(file_name, column_number):

    """
    Gets user-specified column from file and returns it as a list

    Arguments
    ---------
    file_name : str
        name of file to pull column from
    col_num : int
        column to calculate mean and stdev

    Returns
    ---------
    column_values : list of int
        list of values from user-specified column
    """

    file = open(file_name, 'r')
    column_values = []
    for line in file:
        row_values = [int(value.strip()) for value in line.split()]
        column_values.append(row_values[column_number])

    return column_values


def column_mean(column_values):

    """
    Finds the mean of a list of column values

    Arguments
    ---------
    column_values : list of int
        list of values from a user-specified column

    Returns
    ---------
    mean : float
        mean of a list of values
    """

    mean = sum(column_values)/len(column_values)
    return mean


def column_stdev(column_values):

    """
    Finds the standard deviation of a list of column values

    Arguments
    ---------
    column_values : list of int
        list of values from a user-specified column

    Returns
    ---------
    stdev : float
        standard deviation of a list of values
    """

    stdev = math.sqrt(
        sum([(mean-x)**2 for x in column_values]) / len(column_values))
    return stdev


if __name__ == '__main__':

    args = parse_arguments()

    try:
        column_values = get_column_from_file(args.filename, args.column_number)
    except FileNotFoundError:
        print('Could not find ' + args.filename)
        sys.exit(1)
    except PermissionError:
        print('Could not open ' + args.filename + ' due to permissions')
        sys.exit(1)
    except ValueError:
        print('Non-integer entry in ' + args.filename)
        sys.exit(1)
    except IndexError:
        print('Column ' + str(args.column_number) + ' out of range of ' /
              + args.filename)
        sys.exit(1)

    try:
        mean = column_mean(column_values)
        print('mean:', mean)
        stdev = column_stdev(column_values)
        print('stdev:', stdev)
    except ZeroDivisionError:
        print('Cannot divide by zero')
        sys.exit(1)
    except ValueError:
        print('Cannot take the sqrt of negative number')
        sys.exit(1)
