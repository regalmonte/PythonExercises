# python AutoTester.py <testfilename>
# example:
# python tester/AutoTester.py max_pairwise_product.test

import sys
import os
import re
import random
import time
MAX_ARR_LEN_SLOW = 1000
MAX_VAL_SLOW = 10000
Verbose = 0


class TestInput:
    def __init__(self, input_info):
        self.details = {}
        for detail in (input_info[1:-1:]).split(","):
            detail_arr = (detail.strip()).split(":")
            self.details.update({detail_arr[0]:detail_arr[1]})


class Tester:
    def __init__(self, test_file_name):
        self.fname = "./tests/" + test_file_name
        self.directory = ""
        self.filename = ""
        self.functionname = ""
        self.verifyfunction = ""
        self.numberofinputs = 0
        self.numberoftests = 1000
        self.inputList = []
        self.condition = ""

    def readFile(self):
        with open(self.fname) as f:
            content = f.readlines()
        return [x.strip() for x in content]

    def parseTestFile(self):
        content = self.readFile()
        for l in content:
            if l.find("#") == 0:
                continue
            if l.find("=") < 0:
                continue
            info = l.split("=")
            input_pattern = re.compile('input[0-9]+$')
            if info[0] == "directory":
                self.directory = info[1]
            elif info[0] == "filename":
                self.filename = info[1]
            elif info[0] == "functionname":
                self.functionname = info[1]
            elif info[0] == "verifyfunction":
                self.verifyfunction = info[1]
            elif info[0] == "numberofinputs":
                self.numberofinputs = info[1]
            elif info[0] == "numberoftests":
                self.numberoftests = info[1]
            elif input_pattern.match(info[0]):
                self.inputList.append(TestInput(info[1]))
            elif info[0] == "condition":
                self.condition = info[1]

    def printTestSummary(self):
        print("Test Summary:")
        print("test file:", self.fname)
        print("directory:", self.directory)
        print("file to test:", self.filename)
        print("function to test:", self.functionname)
        print("number of inputs:", self.numberofinputs)
        for inp in self.inputList:
            print("input entry:", inp.details)

    def generateInput(self, i, mode="Fast"):
        input_dictionary = self.inputList[i].details
        if input_dictionary['type'] == 'array':
            arr_len0 = strToInt(input_dictionary['lenrange0'])
            arr_len1 = strToInt(input_dictionary['lenrange1'])
            arr_val0 = strToInt(input_dictionary['valuerange0'])
            arr_val1 = strToInt(input_dictionary['valuerange1'])
            arr_len1 = MAX_ARR_LEN_SLOW if mode == "Slow" else arr_len1
            arr_len = int(random.uniform(arr_len0, arr_len1))
            res = []
            for j in range(arr_len):
                res.append(int(random.uniform(arr_val0, arr_val1)))
            return res
        else: #if input_dictionary['type'] == 'int':
            arr_val0 = strToInt(input_dictionary['valuerange0'])
            arr_val1 = strToInt(input_dictionary['valuerange1'])
            arr_val1 = MAX_VAL_SLOW if mode == "Slow" else arr_val1
            return int(random.uniform(arr_val0, arr_val1))

    def runOneTest(self, funcName, test_input):
        sys.path.insert(0, self.directory)
        test_module = __import__(self.filename)
        test_function = eval("test_module." + funcName)
        numOfInputs = int(self.numberofinputs)
        if numOfInputs == 1:
            return test_function(test_input[0])
        elif numOfInputs == 2:
            test_input = self.checkCondition(test_input)
            return test_function(test_input[0], test_input[1])
        elif numOfInputs == 3:
            return test_function(test_input[0], test_input[1], test_input[3])
        else:
            raise ValueError("Testing of function with more than 3 inputs is not yet implemented")

    def checkCondition(self, testinput):
        if (self.condition == "input2>input1" and testinput[0] > testinput[1]) or \
                (self.condition == "input1>input2" and testinput[1] > testinput[0]):
            return tuple([testinput[1], testinput[0]])
        return testinput

    def verifyTest(self):
        for i in range(int(self.numberoftests)):
            test_input = ()
            for j in range(int(self.numberofinputs)):
                test_input = test_input + (self.generateInput(j, 'Slow'),)

            if Verbose > 1:
                print("Test Input:", test_input)
            s1 = self.runOneTest(self.functionname, test_input)
            if Verbose > 1:
                print("Solution:", s1)
            s2 = self.runOneTest(self.verifyfunction, test_input)
            if Verbose > 1:
                print("Verifier:", s2)
            if s1 != s2:
                if self.inputList[0].details['type'] == 'int':
                    print("Test", test_input, ": NG", s1, s2)
                else:
                    print("Test", i, ": NG", s1, s2)
                return False
            else:
                if self.inputList[0].details['type'] == 'int':
                    print("Test", test_input, ": OK", s1, s2)
                else:
                    print("Test", i, ": OK", s1, s2)
        print("Done Verification Test")
        return True

    def stressTest(self):
        start_time = time.time()
        n = int(self.numberoftests)
        for i in range(n):
            test_input = ()
            for j in range(int(self.numberofinputs)):
                test_input = test_input + (self.generateInput(j),)
            print("test_input", i, ":", test_input, ":", end=" ")
            s1 = self.runOneTest(self.functionname, test_input)
            print(s1)
        print("\n\nAverage run time: %s seconds" % ((time.time() - start_time)/n))


def strToInt(s):
    if "*" in s:
        return eval(s)
    else:
        return int(s)

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    test = Tester(sys.argv[1])
    test.parseTestFile()
    test.printTestSummary()
    if test.verifyTest():
        test.stressTest()
    #content = readFile("./tests/" + sys.argv[1])
    #prepareTest(content)

