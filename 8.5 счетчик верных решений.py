n = int(input())
answers = set()
counter = 0
for i in range(n):
    answer = input()
    if answer[-1] == 't': answers.add(answer); counter += 1
if counter > 0:
    print(f'Верно решили {len(answers)} учащихся')
    print(f'Из всех попыток {int((counter/n*100)+.5)}% верных')
else: print('Вы можете стать первым, кто решит эту задачу')