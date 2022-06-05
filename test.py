def testMethod(myword):
    #print(myword)
    #print (myword[0:7])
    i=len(myword)-1;
    reversed=""
    while (i>=0):
        print(myword[i])
        reversed+=myword[i]
        i-=1
        
    print(reversed)


#if __file__== "test.py":
#    testMethod("mytest")

testMethod("anar")