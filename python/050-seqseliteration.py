# An example that uses sequence, selection and iteration
password='abcdef'
maxattempts=3

attempts=0
correct=False

while correct == False and attempts<maxattempts:
    print("Enter password:")
    userpassword=input()
    if userpassword == password:
        correct=True
        print("Logged into system")
    else:
        attempts=attempts+1

# We reach this point either if correct is true or attempts>=maxattempts
if correct == False:
    print("Maximum login attempts, goodbye")
    exit()

print("SECRET INFORMATION HERE!")