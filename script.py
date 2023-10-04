def solution(pin):
    adjacent_digits = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9']
    }
    
    def generate_variations(pin, index):
        if index == len(pin):
            variations.append(pin)
            return
        for digit in adjacent_digits[pin[index]]:
            generate_variations(pin[:index] + digit + pin[index+1:], index + 1)
    
    variations = []
    generate_variations(pin, 0)
    return sorted(variations)
    

# Test cases
print(solution("8"))
print(solution("11"))
