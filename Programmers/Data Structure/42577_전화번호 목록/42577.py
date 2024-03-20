def solution(phone_book):
    hash_map = dict()
    
    for phone in phone_book:
        hash_map[phone] = 1
    
    for numbers in phone_book:
        temp = ""
        for number in numbers:
            temp += number
            if temp in hash_map and temp != numbers:
                return False
            
    return True