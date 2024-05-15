def sorter(list_to_sort, reverse=False, key=None):

    if key is not None:
        list_to_sort.sort(key=key, reverse=reverse)
    else:
        list_to_sort.sort(reverse=reverse)

    return list_to_sort

if __name__ == "__main__":

    list_to_sort = [5, 2, 9, 4, 1, 6, 10, 8, 3, 7]
    new_list = sorter(list_to_sort)
    print(new_list)


def sort_string(list_of_strings, reverse=False):


    if reverse:
        list_of_strings.sort(reverse=True)
    else:
        list_of_strings.sort()

    return list_of_strings

strings = ["wechale", "Rahab", "Esther", "Stephen", "Injendi", "Zakayo", "Mwalati"]

sorted_strings = sort_string(strings)

print(sorted_strings)

reversed_strings = "".join(reversed(strings))
print(reversed_strings)