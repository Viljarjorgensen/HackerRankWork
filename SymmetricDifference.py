def symmetric_difference(set_a, set_b):
    difference_set = set_a.symmetric_difference(set_b)
    sorted_list = sorted(difference_set)
    for i in range(len(sorted_list)):
        print(sorted_list[i])



if __name__ == "__main__":
    M = int(input(""))
    a = input("")
    list_a = a.split()
    set_a = list(map(int, list_a))
    set_a = set(set_a)
    N = int(input(" "))
    b = input(" ")
    list_b = b.split()
    set_b = list(map(int, list_b))
    set_b = set(set_b)
    symmetric_difference(set_a, set_b)