class Id_info:
    def __init__(self, Id, Level):
        self.Id=Id
        self.Level=Level
    def say(self):
        print(f'user {self.Id} lv {self.Level}')

id_A=Id_info('codetree', 10)

id_input, level_input= input().split()

id_B=Id_info(id_input, level_input)

id_A.say()
id_B.say()