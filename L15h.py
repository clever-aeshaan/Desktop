def shutdown():
    want = input("do you want to shut down? `yes or no` ")
    if(want == "yes" or "Yes" or "YES"):
        print("shutting down")
    elif(want == "no" or "No" or "NO" ):
        print("aborting shutdown")
    else:
        print("sorry, invalid input")
shutdown()