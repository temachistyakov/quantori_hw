def even_num(input_lst: list):
    input_lst = list(input_lst)
    input_lst_int = []
    for i in input_lst:
        input_lst_int.append(int(i))
    output_lst = []
    for x in input_lst_int:
        mod = x % 2
        if x == 254:
            break
        elif mod == 0:
            output_lst.append(x)
    print(output_lst)


input_lst = input("Type sequence of comma-separated num: ").split(',')
even_num(input_lst)
