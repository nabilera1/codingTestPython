# The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.?
#Returns:
#returns an iterator that is already filtered.

def fun(v):
    letters=['a','e','l','m','n','v']
    if(v in letters):
        return True
    else:
        return False
seq=['l','o','v','e']
ans=filter(fun,seq)
print(ans)
for i in ans:
    print(i)