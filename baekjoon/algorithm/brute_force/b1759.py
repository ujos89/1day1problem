from itertools import combinations

L, C = map(int, input().split())
words = list(map(str, input().split()))

vowels_list = ['a','e','i','o','u']
vowels = []
consonants = []
for word in words:
    if word in vowels_list:
        vowels.append(word)
    else:
        consonants.append(word)

chosed_consonants = list(combinations(consonants, 2))
answer_list = []
for v in vowels:
    for c in chosed_consonants:
        tmp_answer = list(v)
        for _ in c:
            tmp_answer.append(_)

        if L == 3:
            tmp_answer.sort()
            answer_list.append(''.join(tmp_answer))

        else:
            left_words = []
            for word in words:
                if word not in tmp_answer:
                    left_words.append(word)

            chosed_left_words_list = list(combinations(left_words,L-3))
            for chosed_left_words in chosed_left_words_list:
                tmp = []
                for chosed_left_word in list(chosed_left_words):
                    tmp.append(chosed_left_word)
                
                answer = tmp_answer + tmp
                answer.sort()
                answer = ''.join(answer)
                if answer not in answer_list:
                    answer_list.append(answer)

    words.remove(v)

answer_list.sort()
for _ in answer_list:
    print(_)
'''
feedback
나의풀이: 코드 구현을 모음1개, 자음2개를 고르고 나머지 것에서 combination해서 정답을 구했다.
다른풀이: 가능한 모든 정답 집합에서 모음1개, 자음2개 이상인 것을 정답으로 출력했다.
'''