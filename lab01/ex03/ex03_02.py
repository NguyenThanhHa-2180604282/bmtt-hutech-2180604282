def dao_nguoc_list(lst):
    return list(reversed(lst))

input_lst = input("Nhập danh sách các số, cách nhau bằng dấu phẩy:")
numbers = list(map(int, input_lst.split(',')))
list_dao_nguoc = dao_nguoc_list(numbers)
print("Danh sách sau khi đảo ngược: ", list_dao_nguoc)
