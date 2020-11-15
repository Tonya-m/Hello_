import yaml

with open("./data.yaml", 'r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    Test_data = data.get("Test")
    for i in Test_data.keys():
        print("test: %s \n test_name: %s \n test_pwd: %s \n" %
              (i, Test_data.get(i).get("name"), Test_data.get(i).get("pwd")))

data01 = {'Login_Data': {'login_test_001': {'name': '毛毛', 'pwd': 'm123', 'se': '男'}, 'sex': {'se': '男'}}}
with open("./w_data01.yaml", "w") as f:
    w_data = yaml.dump(data01, f, encoding='utf-8', allow_unicode=True)
