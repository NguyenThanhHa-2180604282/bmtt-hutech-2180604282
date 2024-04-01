def tao_tuple_tu_list(lst):
    return tuple(lst)

input_lst = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_lst.split(',')))

my_tuple = tao_tuple_tu_list(numbers)
print("Danh sách: ", numbers)
print("Tuple: ", my_tuple)
