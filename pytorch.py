# line = "0 simplistic , silly and tedious ."
# label, sep, text = line.partition(' ')
# print(label)
# print(sep)
# print(text)



# from torch.autograd import Variable
# import torch
# a = torch.zeros(18)
# a = Variable(a)
# print(a)
# c = 0
# print(a.numel())
# c += a.numel()
# print(c)
# b = torch.randn(1,2,3,4,5)
# print(b)
# print(b.numel())




# def cal_mean(list):
#     sum = 0.0
#     for i in list:
#         print(i)
#         sum += i
#     avg = (sum / len(list))
#     return avg
#
# list = [10.9, 9.9, 8.8]
# mean = cal_mean(list)
# print(mean)




# import torch
# a = torch.FloatTensor([[1, 2], [3, 4]])
# b = torch.FloatTensor([[1, 2], [3, 4]])
# print(a)
# print(b)
# c = torch.mm(a, b)
# print(c)
# d = a.mm(b)
# print(d)




# from torch.autograd import Function, Variable
# import torch
# class sru_com(Function):
#     def __init__(self,b):
#         print("init")
#
#     def forward(self,c):
#         print("forward")
#         return None
#
# x = sru_com(Variable(torch.randn(3,4)))(Variable(torch.randn(3,3)))


# list = [1, 2, 3, 4, 5, 6]
# print(list[-2::-1])
# print(list[-2::-2])
# print(list[-1::-1])

# import time
# start = time.time()
# for i in range(1000000):
#     print(i * 2)
#     print(i * 3 * 8 / 5 - 4)
# end = time.time()
# print("Times: ", end - start)












