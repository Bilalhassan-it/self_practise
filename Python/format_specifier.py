# format specifiers = {value : flag(s)} format a value based on what flags are used. 

# .(number)f = round to that many decimal places
# :number = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate a positive value
# :  = insert a space before positive value
# :, = comma seperator


a = 300012.148623
b = -23100.321
c = 231000.4412

print(f"The value is {a:^+10,}")
print(f"The value is {b:^+10,}")
print(f"The value is {c:^+10,}")