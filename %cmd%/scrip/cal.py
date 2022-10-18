import sys
import time

a = int(input("ได้สัปดาห์ละ: "))
b = int(input("ใช้เงินวันละ(จ-ศ): "))
c = int(input("ต้องการเก็บเงินให้ถึง: "))
we = 0
e = int(we+a)
x = 1
loop_progress = 5
while loop_progress < 6:
    ba = 1
    sa = 5
    d = (e - (b * sa))
    ir = e - b
    cc = a - b
    print("week processes")
    if ir >= c:
        x = x + 1
        ccd = cc * x
        print("ต้องใช้เวลา", x, "สัปดาห์")
        print("จะเก็บได้สัปดาห์ละ", cc)
        print("จะได้เงินทั้งหมด", ccd)
        
        break
    else:
         e = e + a
         x = x + 1
print("You have 1000 second to see the Result")
time.sleep(1000)
sys.exit()