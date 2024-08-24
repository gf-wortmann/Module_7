# Домашнее задание по теме "Форматирование строк"

class Team:
    def __init__(self, name, participants_count, solved_tasks_count, time_to_solve):
        self.name = name
        self.participants_count = participants_count
        self.solved_tasks_count = solved_tasks_count
        self.time_to_solve = time_to_solve


t1 = Team('Мастера кода', 5, 40, 1552.512)
t2 = Team('Волшебники данных', 6, 42, 2153.31451)

print('В команде %s участников %d' % (t1.name, t1.participants_count))
print('Итого сегодня в командах участников: %d and %d!' % (t1.participants_count, t2.participants_count))
# using format
print('Команда {} решила задач: {:d}!'.format(t2.name, t2.solved_tasks_count))
print('{} решили задачи за {:.2f} секунд!'.format(t2.name, t2.time_to_solve))


# using f-strings
def print_winner(name):
    print(f'Победа команды {name}!')


print(f'Команды решили {t1.solved_tasks_count} и {t2.solved_tasks_count} задач.')

if t1.solved_tasks_count > t2.solved_tasks_count or t1.solved_tasks_count == t2.solved_tasks_count and \
        t1.time_to_solve < t2.time_to_solve:
    print_winner(t1.name)
elif t2.solved_tasks_count > t1.solved_tasks_count or t2.solved_tasks_count == t1.solved_tasks_count and \
        t2.time_to_solve < t1.time_to_solve:
    print_winner(t2.name)
else:
    print('Ничья!')

print(f'Сегодня было решено {t1.solved_tasks_count + t2.solved_tasks_count} задач, в среднем по'
      f' {(t1.time_to_solve + t2.time_to_solve) / (t1.solved_tasks_count + t2.solved_tasks_count):.2f}'
      f' секунд на задачу.')
