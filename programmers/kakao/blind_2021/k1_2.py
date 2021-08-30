from itertools import combinations
from collections import Counter

def order2course(idx_list, orders, course_dict):
    order_all = []
    for idx in idx_list:
        order_all.extend(orders[idx])
    order_count = Counter(order_all)

    common_menu = []
    for menu in order_count:
        if order_count[menu] >= 2:
            common_menu.append(menu)
    common_menu = sorted(common_menu)

    if len(common_menu) >= 2:
        for menu_num in course_dict:
            for _ in list(combinations(common_menu, menu_num)):
                course_dict[menu_num].append(_)

    return course_dict

def solution_(orders, course):
    len_orders = len(orders)
    orders_ = []
    for order_ in orders:
        orders_.append([*order_])

    course_dict = {key:[] for key in course}
    for idx_list in combinations(range(len_orders), 2):
        course_dict = order2course(idx_list, orders_, course_dict)

    answer = []
    for menu_num in course_dict:
        if course_dict[menu_num]:
            course_count = Counter(course_dict[menu_num])
            most_common_num = course_count.most_common()[0][1]
            for course_ in course_count:
                if course_count[course_] == most_common_num:
                    answer.append(''.join(list(course_)))

    return sorted(answer)


def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += combinations(sorted(order), course_size)

        most_ordered = Counter(order_combinations).most_common()
        print(most_ordered)
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))