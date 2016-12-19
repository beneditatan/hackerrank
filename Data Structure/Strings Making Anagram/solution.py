def number_needed(a, b):
    counter = 0
    a_list = list(a)
    b_list = list(b)
    
    while (len(b_list) > 0):
        for i in range(len(a_list)):
            if (a_list[i] in b_list):
                counter += 1
                b_list.pop(b_list.index(a_list[i]))
        if (a_list.sort() == b_list.sort()):
            break
            
    num = len(a) + len(b) - 2*counter
    return num
    pass

a = input().strip()
b = input().strip()

print(number_needed(a, b))
