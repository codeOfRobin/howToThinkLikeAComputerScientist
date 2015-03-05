import sys

def parta(x,y):
    i=0
    j=0
    result=[]
    while True:
        if i>=len(x):
            return result
        elif j>=len(y):
            return result
        elif x[i]<y[j]:
            print("i")
            i+=1
        elif x[i]>y[j]:
            print("j")
            j+=1
        elif x[i]==y[j] and x[i]!=result[-1]:
            result.append(x[i])
            print(i)
            print(j)
            i+=1
            j+=1








def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(absolute_value(17) == 17)
    test(parta([1,2,3],[2,3,4])==[2,3])


test_suite()        # Here is the call to run the tests