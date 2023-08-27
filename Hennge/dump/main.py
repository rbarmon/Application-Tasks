import sys

def main():
    """
    Function description: Function to calculate the sum of squares of given integers, excluding any negatives.

    In this function it receives the input and converts the string to int to identify the number of test cases
    which is then passed to the helper function handleTestCases.
    """
    
    sys.stdout.write(handleTestCases(int(sys.stdin.readline().strip())))

def handleTestCases(num_testcases):
    """
    Function description: Helper function for the main function. Takes the total number of test cases as input parameter
    and recursively processes each test case to return as a set of calculated sum(s) in the output.
    """
    if num_testcases == 0:
        return ""
    else:
        result = processTestCase()
        remaining_results = handleTestCases(num_testcases - 1)
        return result + "\n" + remaining_results

def processTestCase():
    """
    Function description: Function to calculate the sum of squares of the integers, excluding any negatives for each test 
    case. Converts test case into a list and applies filter to remove negative values and then maps a function that squares
    the remaining postive values, and finally sums all numbers in the list. 
    """
    num_integers = int(sys.stdin.readline())
    num = sum(list(map(squareNumbers, list(filter(removeNegativeVal,list(map(int, sys.stdin.readline().strip().split())))))))
    return str(num)

def removeNegativeVal(number):
    """
    Function description: Function that returns False if a value is negative and return True if positive.
    """
    if number < 0:
        return False
    else:
        return True

def squareNumbers(number):
    """
    Function description: Function that squares a given input number.
    """
    return number ** 2


if __name__ == '__main__':
    main()



