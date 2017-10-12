"""Lambda expression usage and requirement"""


scientists = ["AB CD", "EF GH", "IJ KL", "MN OP", "DS OW", "sd as", "sdf acpo"]

print(sorted(scientists, key=lambda ls_nm: ls_nm.split()[-1], reverse=True))
last_name = lambda nm: nm.split()[-1]
print(last_name)
