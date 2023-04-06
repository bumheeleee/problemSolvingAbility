def solution(phone_book):
    answer = True
    
    phone_book.sort()
    for elem1, elem2 in zip(phone_book, phone_book[1:]):
        if elem2.startswith(elem1):
            answer = False
            break
    return answer

print(solution(["119", "97674223", "1195524421"]))