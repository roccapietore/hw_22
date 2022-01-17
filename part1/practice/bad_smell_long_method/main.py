# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля

csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def _read(file):
    file_list = []
    for line in file.split('\n'):
        name, age = line.split(';')
        file_list.append([name, int(age)])
    return file_list


def _sort(data):
    return sorted(data, key=lambda x: int(x[1]))


def _filter(some_list):
    result_data = []
    for person in some_list:
        if person[1] > 10:
            result_data.append(person)
    return result_data


def get_users_list():
    data = _read(csv)
    sort_list = _sort(data)
    result = _filter(sort_list)
    return result


if __name__ == '__main__':
    print(get_users_list())
