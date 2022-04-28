salute_pairs = []

def filter_salutes(salute_pairs):
    for i in salute_pairs:
        comparing_list = salute_pairs
        comparing_list.remove(i)
        for j in comparing_list:
            if j.reverse() == i:
                salute_pairs.pop(j)
    return salute_pairs
            
def solution(s):
    trimmed_hall = s.strip("-")
    for x, char in enumerate(trimmed_hall):
        if char == ">":
            chars_in_path = trimmed_hall[x+1:]
            for char_in_path in chars_in_path:
                if char_in_path == "<":
                    salute_pair = [x, char_in_path]
                    salute_pairs.append(salute_pair)
        elif char == "<":
            chars_in_path = trimmed_hall[:x]
            for char_in_path in chars_in_path:
                if char_in_path == ">":
                    salute_pair = [x, char_in_path]
                    salute_pairs.append(salute_pair)
    
    filtered_salute_pairs = filter_salutes(salute_pairs)
    num_of_salutes = (len(filtered_salute_pairs)) * 2
    return num_of_salutes
    
            
print(solution("-<><><<-"))           
    
        