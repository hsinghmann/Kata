def binrota(arr):
    l = []
    for i in range(len(arr)):
        if i % 2 == 0:
            l.extend(arr[i])
        else:
            l.extend(arr[i][::-1])
    print l

binrota([["Stefan", "Raj", "Marie"],
["Alexa", "Amy", "Edward"],
["Liz", "Claire", "Juan"],
["Dee", "Luke", "Katie"]])


