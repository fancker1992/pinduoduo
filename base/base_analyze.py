import yaml


def analyze_with_file(file_name, case_name):
    print("./data/" + file_name + ".yml")
    with open("./data/" + file_name + ".yml", "r", encoding='UTF-8') as f:
        res = yaml.load(f)[case_name]

        temp_list = list()
        for values in res.values():
            temp_list.append(values)

        return temp_list

# [{'username': 'zhangsan', 'password': 'zhangsan123'}, {'username': 'lisi', 'password': 'lisi123'}, {'username': 'wangwu', 'password': 'wangwu123'}]
