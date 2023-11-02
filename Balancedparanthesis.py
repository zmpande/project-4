#Challenge 4
#Balanced Parantheses in an expression

open_para = ["[","(","{"]
close_para = ["]",")","}"]

def balanced_para(mypara):
    #database(Stack) where parantheses will be stored, check last added and match
    s = []
    for i in mypara:
        if i in open_para:
            #storing the parantheses into database
            s.append(i)
        elif i in close_para:
            para = close_para.index(i)
            #s[-1] is last open para and mypara[i] is the first close para
            if ((len(s)>0) and (open_para[para] ==s[len(s)-1])):
              #pop out to remove matching parantheses from database
                s.pop()
            else:
                return "False"
    #parantheses matched then database will be empty
    if len(s)==0:
        return "True"
    #database is not empty
    else:
        return "False"

mypara = input("Please enter the paranthesis: ")
print(balanced_para(mypara))
