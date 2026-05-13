# avg definition
def avg(a, b):
    return (a + b) / 2
# avg call
print(avg(10, 20))

# check type of fuction
name = "Sabbir Hassan"
roll = 101
print(type(name))
print(type(roll))

# converter function
def conveter(usd_val):
    inr_val = usd_val * 82.74
    print(f"{usd_val} USD is equal to {inr_val} INR")

conveter(100)