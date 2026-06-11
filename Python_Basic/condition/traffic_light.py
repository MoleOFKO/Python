print("------Traffic Light Program------")
#variable Declaration from user
light = input("Enter the traffic light color (Green , Yellow , Red) : ").lower()
if light == "green":
    print("Go")
elif light == "yellow":
    print("Slow Down")
elif light == "red":
    print("Stop")
else:
    print("Invalid Traffic Light Color")
