# Day 20 - What Can Range really do?
print("== List Generator ==")
print()
start = int(input("Start at: "))
end = int(input("End before: "))
increment = int(input("Increment between values: "))
print()
for i in range(start, end, increment):
    print(i)
