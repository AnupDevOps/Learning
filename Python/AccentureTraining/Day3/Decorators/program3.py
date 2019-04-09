# Example 3rd

def Mydecorator(somefunction):
    def around():
        print("PRE TASK")


        somefunction()

        print("Post task")
    return around

@Mydecorator
def MyFun():
    print("Function doing some task")

#call = Mydecorator(MyFun)
#call()


MyFun()
