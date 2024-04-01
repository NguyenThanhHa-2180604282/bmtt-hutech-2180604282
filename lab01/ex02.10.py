def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]

input_String = input("Moi nhap chuoi can dao nguoc: ")
print ("Chuoi dao nguoc la:",dao_nguoc_chuoi(input_String))