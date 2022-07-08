# Deep flatten of the said list of integers
# o/p [1, 2, 3, 4, 5, 6]
#said_list = [1, [2], [[3], [4], 5], 6]
#said_list = [[[1, 2, 3], [4, 5]], 6]
said_list = [1,2,3,[[[4]]],[5,6]]
at_Length = []
LIST = []
def Flatten(said_list):
    for i in said_list:
        if type(i)==int:
            at_Length.append(i)
        elif type(i)== list:
            Flatten(i)
    return at_Length
LIST = Flatten(said_list)           
print(LIST)