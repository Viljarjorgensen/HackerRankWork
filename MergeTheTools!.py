def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i + k]

        result = ""
        for char in substring:
            if char not in result:
                result += char
        print(result)




if __name__ == '__main__':
    merge_the_tools("AABCAAADA", 3)