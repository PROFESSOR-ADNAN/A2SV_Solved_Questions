def is_capital_letter(character):
    return ord("A") <= ord(character) <= ord("Z")

def is_small_letter(character):
    return ord("a") <= ord(character) <= ord("z")

def small_to_capital(character):
    return chr(ord(character) - 32)
    
def capital_to_small(character):
    return chr(ord(character) + 32)

def swap_case(s):
    answer = ""
    for char in s:
        if is_capital_letter(char):
            answer += capital_to_small(char)
        elif is_small_letter(char):
            answer += small_to_capital(char)
        else:
            answer += char
    
    return answer
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)