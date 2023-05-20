

class Student:
    def __int__(self, name="ss", student_id="90"):
        self.name = name
        self.student_id = student_id
        self.grades = {"语文": 0, "数学": 0, "英语": 0}
    # print("构造函数1运行")

    # def __int__(self,s_name,s_sid):
    #     self.name = s_name
    #     self.sid = s_sid
    #     self.chi = 0
    #     self.eng = 0
    #     self.mat = 0
    #     print("构造函数2运行")
    # def setGrade(self, s_chi, s_eng, s_mat):
    #     self.chi = s_chi
    #     self.eng = s_eng
    #     self.mat = s_mat
    #     print("成功设置成绩")
    #
    # def show(self):
    #     print("语文成绩：" + str(self.chi) + "数学成绩：" + str(self.mat) + "英语成绩：" + str(self.eng))


s1 = Student()
# s1.show()
print(s1.name)
print(s1.grades)
