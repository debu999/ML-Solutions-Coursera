print("Hello")
for indx in range(1,11,2):
    print("Printing Odd Line {0}".format(indx))

std = {"nm":"Ramu","dob":"12-Jan-1987","city":"Berhampur","cur_loc":"Singapore","last_name":"Kaka"}

try:
    last_nm = std["last_name"]
    sum = last_nm + 3
except KeyError:
    print("Handling Key Error in Except Block")
    last_nm = "Not Found"
except TypeError as terr:
    print("Can't add string {} to {} ".format(last_nm,3)," Error encountered is {}".format(terr))
print(last_nm)