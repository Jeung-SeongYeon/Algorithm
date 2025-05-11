def check_prefix(phone_book):
    pre_dict = {}
    for num in phone_book:
        if not pre_dict:
            pre_dict[len(num)] = [num]
        else:
            for key in pre_dict.keys():
                for phone in pre_dict[key]:
                    if num[:key] == phone:
                        return False
            pre_dict[len(num)] = [num]
    return True

def solution(phone_book):
    phone_book.sort()
    answer = check_prefix(phone_book)
    
    return answer