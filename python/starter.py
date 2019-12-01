import aocd
import os
import datetime


class Starter():
    input_template = "c:/aoc/inputs/%s/day_%s.txt"

    def __init__(self, year=None, day=None):
        self.aocd_data = ""
        self.set_date(year, day)
        self.set_input_file()

    def set_date(self, year, day):
        now = datetime.datetime.now()
        self.year = year or now.year
        self.day = day or now.day

    def set_input_file(self):
        self.input_file_path = self.input_template % (self.year, self.day)
        if not os.path.exists(self.input_file_path):
            print("importing data...")
            self.aocd_data = aocd.get_data(year=self.year, day=self.day)
            with open(self.input_file_path,'w') as input_file:
                input_file.write(self.aocd_data)

        # print(self.input_file_path)

    def read_from_input_file(self):
        with open(self.input_file_path,"r") as input_file:
            z =  input_file.readlines()
        return z

class MyTestCase():
    def __init__(self, input, solution):
        self.input = input
        self.solution = solution


class Solution():
    test_template = "Result: %s, %s expected, got: %s"

    def __init__(self, f):
        self.test_cases = []
        self.fun = f

    def solution(self, input):
        return self.fun(input)

    def add_test_case(self, case: MyTestCase):
        self.test_cases.append(case)

    def test_me(self):
        passing = True
        if self.test_cases == []: passing = False
        for t in self.test_cases:
            answer = self.solution(t.input)
            passing = passing and t.solution == answer
            test_result = self.test_template % (t.solution == answer, t.solution, answer)
            print(test_result)

        return passing

# input = 'c:/aoc/inputs/%s/day%s.txt' % (year,day)
# print(input)
#

if __name__ == "__main__":
    s = Starter()
