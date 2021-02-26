import sys
input = sys.stdin.readline
cards_num = int(input())
cards = list(map(int, input().split()))
questions_num = int(input())
questions = list(map(int, input().split()))

cards_dict = {}
for card in cards:
    if card in cards_dict:
        cards_dict[card] += 1
    else:
        cards_dict[card] = 1

answer = []
for question in questions:
    if question in cards_dict:
        answer.append(cards_dict[question])
    else:
        answer.append(0)

print(*answer)