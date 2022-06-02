def sorter(input_list):
    is_int = [x for x in input_list if isinstance(x, int)]
    non_int = [x for x in input_list if not isinstance(x, int)]
    is_int.sort(reverse=True)
    is_int = is_int[0:3]
    print(f'Top-three max int {is_int}')
    print(f'You have passed some extra elements that I can not parse {non_int}')


a = [7, 228, 13.37, 2211.22, 3456, 443.33, 'apple', 322, 'dog']
sorter(a)
