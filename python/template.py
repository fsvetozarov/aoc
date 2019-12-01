from starter import Starter, MyTestCase, Solution

def fun_solution1(input):
    return None #str(result)

def fun_solution2(input):
    return None #str(result)

def test_solution1(input):
    solution1 = Solution(fun_solution1)
    # solution1.add_test_case(MyTestCase([],""))
    # solution1.add_test_case(MyTestCase([],""))
    # solution1.add_test_case(MyTestCase([],""))
    # solution1.add_test_case(MyTestCase([],""))
    # solution1.add_test_case(MyTestCase([],""))

    solution1_test = solution1.test_me()

    if solution1_test:
        print(solution1.solution(input))

    return solution1_test

def test_solution2(input):
    solution2 = Solution(fun_solution2)
    # solution2.add_test_case(MyTestCase([],""))
    # solution2.add_test_case(MyTestCase([],""))
    # solution2.add_test_case(MyTestCase([],""))
    # solution2.add_test_case(MyTestCase([],""))
    # solution2.add_test_case(MyTestCase([],""))

    solution2_test = solution2.test_me()

    if solution2_test:
        print(solution2.solution(input))

def test_day():
    input = Starter(2018, 1).read_from_input_file()
    if test_solution1(input):
        test_solution2(input)


if __name__ == "__main__":
    test_day()







