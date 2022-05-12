import re
import datetime
from subprocess import (
    run, PIPE
)


def parse():
    result = run(["ps", "aux"], stderr=PIPE, stdout=PIPE)
    splitted_by_lines = result.stdout.decode().split('\n')
    splitted_by_cols = []

    for line in splitted_by_lines:
        value = re.split(r'[\t ]+', line.strip(), maxsplit=10)
        splitted_by_cols.append(value)

    users = []
    set_users = []
    processes = []
    user_processes = {}
    ram_dict = {}
    cpu_dict = {}
    ram = 0
    cpu = 0
    count = 0
    current_date = datetime.datetime.now()
    current_date_string = current_date.strftime('%d-%m-%y-%H:%M:%S')
    filename = f'{current_date_string}-scan.txt'

    for value in splitted_by_cols[1::]:
        if len(value) > 1:
            processes.append(value[1])
            users.append(value[0])
            if value[0] in user_processes:
                user_processes[value[0]] += 1
            else:
                user_processes[value[0]] = 1
            ram_dict[(value[10], count)] = float(value[3])
            cpu_dict[(value[10], count)] = float(value[2])
            count += 1
        else:
            break

    for k, v in ram_dict.items():
        ram += float(v)

    for k, v in cpu_dict.items():
        cpu += float(v)

    for user in set(users):
        set_users.append(user)

    sorted_ram_dict = dict(sorted(ram_dict.items(), key=lambda item: item[1]))
    sorted_cpu_dict = dict(sorted(cpu_dict.items(), key=lambda item: item[1]))
    max_ram = list(sorted_ram_dict.items())[-1][0][0]
    max_cpu = list(sorted_cpu_dict.items())[-1][0][0]

    with open(filename, 'w') as file:
        file.write('Отчет о состоянии системы:\n')
        file.write(f'Пользователи системы: {", ".join(set_users)}\n')
        file.write(f'Процессов запущено:, {len(processes)}\n')
        file.write('Пользовательских процессов:\n')
        for k, v in user_processes.items():
            file.write(f'{k}: {v}\n')
        file.write(f'Всего памяти используется: {round(ram, 1)}%\n')
        file.write(f'Всего CPU используется: {round(cpu, 1)}%\n')
        file.write(f'Больше всего памяти использует: ({max_ram[:20]})\n')
        file.write(f'Больше всего CPU использует: ({max_cpu[:20]})\n')

    print('Отчет о состоянии системы:')
    print(f'Пользователи системы: {", ".join(set_users)}')
    print(f'Процессов запущено:, {len(processes)}')
    print('Пользовательских процессов:')
    for k, v in user_processes.items():
        print(k, v, sep=': ')
    print(f'Всего памяти используется: {round(ram, 1)}%')
    print(f'Всего CPU используется: {round(cpu, 1)}%')
    print(f'Больше всего памяти использует: ({max_ram[:20]})')
    print(f'Больше всего CPU использует: ({max_cpu[:20]})')


if __name__ == '__main__':
    parse()
