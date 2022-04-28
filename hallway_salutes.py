salute_pairs = []

def trim(hall):
    string_vers = ""
    has_been_right = False
    has_been_left = False
    list_vers = list(hall)
    for x, char in enumerate(list_vers):
        if char == ">":
            has_been_right = True
        if char == "<" and not has_been_right:
            list_vers.pop(x)
            list_vers.insert(x, "-")
                
    for x, char in enumerate(list_vers[::-1]):
        if char == "<":
            has_been_left = True
        if char == ">" and not has_been_left:
            list_vers.pop(x)
            list_vers.insert(x, "-")
    
    for i in list_vers:
        string_vers += i
    return string_vers

def filter_salutes(salute_pairs):
    for i in salute_pairs:
        comparing_list = salute_pairs
        comparing_list.remove(i)
        for j in comparing_list:
            if j.reverse() == i:
                salute_pairs.pop(j)
    return salute_pairs
            
def solution(s):
    trimmed_hall = trim(s)
    for x, char in enumerate(trimmed_hall):
        if char == ">":
            chars_in_path = trimmed_hall[x+1:]
            for approching_char in chars_in_path:
                if approching_char == "<":
                    salute_pair = [x, approching_char]
                    salute_pairs.append(salute_pair)
        elif char == "<":
            chars_in_path = trimmed_hall[:x]
            for approching_char in chars_in_path:
                if approching_char == ">":
                    salute_pair = [x, approching_char]
                    salute_pairs.append(salute_pair)
    
    filtered_salute_pairs = filter_salutes(salute_pairs)
    num_of_salutes = (len(filtered_salute_pairs)) * 2
    return num_of_salutes
    
            
print(solution("-<><><<-"))           
    
        