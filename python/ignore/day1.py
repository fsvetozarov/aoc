from starter import Starter, MyTestCase

class Solution():
    test_template = "Result: %s, %s expected, got: %s"
    # test_cases.append(MyTestCase([],""))

    def __init__(self, f):
        self.test_cases = []


def solution1(input):
    result = 0

    for i in input:
        result += int(i)

    return str(result)






    def test_cases_1(self):
        test_cases = []
        test_cases.append(MyTestCase([+1,+1,+1],"3"))
        test_cases.append(MyTestCase((+1,+1,-2),"0"))
        test_cases.append(MyTestCase((-1,-2,-3),"-6"))

        return test_cases

    def test_cases_2(self):
        test_cases = []
        test_cases.append(MyTestCase([+1,-1], "0"))
        test_cases.append(MyTestCase([+3,+3,+4,-2,-4],"10"))
        test_cases.append(MyTestCase([-6,+3,+8,+5,-6],"5"))
        test_cases.append(MyTestCase([+7,+7,-2,-7,-4],"14"))

        return test_cases

    def test_solution(f):
        passing = True
        for t in test_cases:
            temp_sol = f(t.input)
            passing = passing and t.solution == temp_sol
            test_result = test_template % (t.solution == temp_sol, t.solution, temp_sol)
            print(test_result)




def solution2(input):
    return None



    # if passing:
    #     s = Starter(2018,1)
    #     print(solution1(s.read_from_input_file()))

    return passing

def test_day():
    starter = Starter(2018,1)
    input_data = s.read_from_input_file()
    t1 = test_solution(solution1)

    if t1:
        print(solution1(input_data))
        t2 = test_solution(solution2)

        if t2:
            print(solution2(input_data))

if __name__ == "__main__":
    test_day()







