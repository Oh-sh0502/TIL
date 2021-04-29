def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: len(x))
    print(phone_book)
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in phone_book[phone_book.index(phone_number)+1:] and temp != phone_number:
                return False
    return answer
print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))



# 다른사람 풀이 (startswith을 이용)
# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)
#
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True

# 다른 사람 풀이 (해시 풀이)
# def solution(phone_book):
#     answer = True
#     hash_map = {}
#     for phone_number in phone_book:
#         hash_map[phone_number] = 1
#     for phone_number in phone_book:
#         temp = ""
#         for number in phone_number:
#             temp += number
#             if temp in hash_map and temp != phone_number:
#                 return False
#     return answer

# 다른 사람 풀이 (길이 중심으로 sort)
# def solution(phoneBook):
#     phoneBook.sort(key=lambda x: len(x))
#     for a in range(len(phoneBook)):
#         for b in range(a+1, len(phoneBook)):
#             if phoneBook[b][:len(phoneBook[a])] == phoneBook[a]:
#                 return False
#     return True