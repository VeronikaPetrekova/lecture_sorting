import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))

    return data


def selection_sort(seznam):
    x = len(seznam)
    for i in range(x):
        min_idx = i
        for num_idx in range(i + 1, x):
            if seznam[num_idx] < seznam[min_idx]:
                min_idx = num_idx
        seznam[i], seznam[min_idx] = seznam[min_idx], seznam[i]
    return seznam


def bubble_sort(seznam):
    x = len(seznam)
    for i in range(x-1):
        for index in range(x-i-1):
            if seznam[index] > seznam[index+1]:
                seznam[index], seznam[index+1] = seznam[index+1], seznam[index]
    return seznam


def insertion_sort(seznam_c):
    x = len(seznam_c)
    for i in range(1, x):
        number = seznam_c[i]
        k = i - 1
        while k >= 0 and seznam_c[k] > number:
            seznam_c[k+1] = seznam_c[k]
            k = k - 1
        seznam_c[k+1] = number
    return seznam_c


def main():
    my_data = read_data("numbers.csv")
    o = insertion_sort(my_data["series_2"].copy())
    print(my_data["series_2"])
    print(o)


if __name__ == '__main__':
    main()
