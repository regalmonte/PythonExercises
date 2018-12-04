# python AutoTester.py <testfilename>
# example:
# python tester/AutoTester.py test/max_pairwise_product.test

import sys
import os
import re
import random
import time

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
        self.numberofinputs = 0
        self.inputList = []

    def readFile(self):
        with open(self.fname) as f:
            content = f.readlines()
        return [x.strip() for x in content]

    def parseTestFile(self):
        content = self.readFile()
        for l in content:
            info = l.split("=")
            input_pattern = re.compile('input[0-9]+$')
            if info[0] == "directory":
                self.directory = info[1]
            elif info[0] == "filename":
                self.filename = info[1]
            elif info[0] == "functionname":
                self.functionname = info[1]
            elif info[0] == "numberofinputs":
                self.numberofinputs = info[1]
            elif input_pattern.match(info[0]):
                self.inputList.append(TestInput(info[1]))

    def printTestSummary(self):
        print("Test Summary:")
        print("test file:", self.fname)
        print("directory:", self.directory)
        print("file to test:", self.filename)
        print("function to test:", self.functionname)
        print("number of inputs:", self.numberofinputs)
        for inp in self.inputList:
            print("input entry:", inp.details)

    def generateInput(self, i):
        input_dictionary = self.inputList[i].details
        if input_dictionary['type'] == 'array':
            arr_len0 = strToInt(input_dictionary['lenrange0'])
            arr_len1 = strToInt(input_dictionary['lenrange1'])
            arr_val0 = strToInt(input_dictionary['valuerange0'])
            arr_val1 = strToInt(input_dictionary['valuerange1'])

            arr_len = int(random.uniform(arr_len0, arr_len1))
            res = []
            for j in range(arr_len):
                res.append(int(random.uniform(arr_val0, arr_val1)))
            return res
        else:
            return int(random.uniform(0, 10**3))

    def runOneTest(self):
        sys.path.insert(0, self.directory)
        test_module = __import__(self.filename)
        test_function: function = eval("test_module." + self.functionname)
        test_input = self.generateInput(0)
        test_function(test_input)

    def stressTest(self):
        start_time = time.time()
        for i in range(10**3):
            self.runOneTest()
        print("\n\nTotal run time: %s seconds" % (time.time() - start_time))


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
    test.stressTest()
    #content = readFile("./tests/" + sys.argv[1])
    #prepareTest(content)

