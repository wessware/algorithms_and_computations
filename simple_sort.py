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