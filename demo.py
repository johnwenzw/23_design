# !/usr/bin/env python 
# -*- coding:utf-8 -*-

"""

    author： John wen
    date： 2017-8-1
    description：
    输入两个数和运算符号，得出结果
    工厂模式

"""

class Operation(object):
    def __init__(self, num_a, num_b):
        self._num_a = num_a
        self._num_b = num_b

    def getResult(self):
        pass

class Operation_add(Operation):
    def __init__(self, num_a, num_b):
        super().__init__(num_a, num_b)
    def getResult(self):
        return self._num_a + self._num_b


class Operation_des(Operation):
    def __init__(self, num_a, num_b):
        super().__init__(num_a=num_a, num_b=num_b)

    def getResult(self):
        return self._num_b-self._num_a

class Operation_multi(Operation):
    def __init__(self,num_a, num_b):
        super().__init__(num_a,num_b)
    def getResult(self):
        return self._num_a * self._num_b

class Operation_div(Operation):
    def __init__(self, num_a, num_b):
        super().__init__(num_a, num_b)
    def getResult(self):
        try:
           return  self._num_a / self._num_b
        except:
            raise ZeroDivisionError('The second num can\'t be zero')

class operation_factor(object):
    def __init__(self, operator, num_a, num_b):
        self._operation = operator
        self._num_a = num_a
        self._num_b = num_b

    def createOperate(self):
        if self._operation == '+':
            result = Operation_add(self._num_a, self._num_b)
            return result
        elif self._operation == '-':
            result = Operation_des(self._num_a, self._num_b)
            return result
        elif self._operation == 'x':
            result = Operation_multi(self._num_a, self._num_b)
            return result
        elif self._operation == '/':
            result = Operation_div(self._num_a, self._num_b)
            return result


class windows(object):
    def __init__(self):
        pass

    def set_windows(self):
        self._num_a = int(input('Enter the first number: '))
        self._operation = input('Enter the operator: ')
        self._num_b = int(input("Enter the second number: "))
        operate = operation_factor(self._operation, self._num_a, self._num_b)
        result = operate.createOperate().getResult()
        return result

    def get_num_a(self):
        return self._num_a

    def get_num_b(self):
        return self._num_b

    def get_operate(self):
        return self._operation


if __name__ == '__main__':
    cal = windows()
    r = cal.set_windows()
    print('%s %s %s = %s'%(cal.get_num_a(),cal.get_operate(),cal.get_num_b(),r))





