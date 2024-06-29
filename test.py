if __name__ == '__main__':
            grad = list(range(100))
            lengthOfList = 0
            newList = []
            f = True
            while grad.__len__() != lengthOfList:
                if lengthOfList > grad.__len__():
                    for i in range(0,(grad.__len__())*2,2):
                        grad.insert(i,grad[i])
                else:
                    fw = 0
                    bw = 0
                    r = 0
                    while lengthOfList < grad.__len__():
                                    
                        if r >= grad.__len__()-1:
                            r = 0
                        if f:
                            grad.remove(grad[int(fw-r)])
                            f = False
                        else:
                            grad.remove(grad[int(bw+r)])
                            f = True
                        r = r+1


print(grad)
print([1].__len__())

            # if lengthOfList > length:
            #     remains = lengthOfList - length
            #     it = 0
            #     grad.reverse()
            #     while grad.__len__() <= lengthOfList:  
            #         for index, item in enumerate(grad):
            #             for x in range(2):
            #                 fil.append(item)
            #         if fil.__len__() > lengthOfList:
            #             grad = [i for i in fil]
            #             fil = []
            #             break
            #         grad = [i for i in fil]
            #         fil = []
            #     grad.reverse()
            # if lengthOfList < grad.__len__():
            #     remains = length - lengthOfList
            #     i = 0
            #     while grad.__len__() >lengthOfList:
            #             i = i + 1
            #             if i >= grad.__len__()-1:
            #                 i = 1
            #             grad.remove(grad[i-1])