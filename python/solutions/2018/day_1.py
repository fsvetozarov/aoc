from starter import Starter, MyTestCase, Solution

def fun_solution1(input):
    #  result = sum(map(int,input)) - quick, but too quick
    result = 0
    for i in input:
        result += int(i)
    return str(result)

def fun_solution2(input):
    freq = 0
    past_freqs = {freq}

    while True:
        for i in input:
            freq += int(i)
            if freq in past_freqs:
                return str(freq)
            past_freqs.add(freq)



def test_solution1(input):
    solution1 = Solution(fun_solution1)
    solution1.add_test_case(MyTestCase([1,-2,3,1],"3"))
    solution1.add_test_case(MyTestCase([+1,+1,+1],"3"))
    solution1.add_test_case(MyTestCase([1,1,-2],"0"))
    solution1.add_test_case(MyTestCase([-1,-2,-3],"-6"))
    # solution2.add_test_case(MyTestCase([],""))

    solution1_test = solution1.test_me()

    if solution1_test:
        print(solution1.solution(input))

    return solution1_test

def test_solution2(input):
    solution2 = Solution(fun_solution2)
    solution2.add_test_case(MyTestCase([1,-2,3,1],"2"))
    solution2.add_test_case(MyTestCase([+1,-1],"0"))
    solution2.add_test_case(MyTestCase([+3,+3,+4,-2,-4],"10"))
    solution2.add_test_case(MyTestCase([+7,+7,-2,-7,-4],"14"))
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







