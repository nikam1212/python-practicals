import time

print("=== Traffic Signal Simulator ===")

signal = input("Enter the colour of signal (red/yellow/green): ").lower()

if signal == "red":
    print("\n🔴 RED SIGNAL")
    
    
    for i in range(5, 0, -1):
        print("Timer:", i, "seconds")
        time.sleep(1)
        print("STOP")
elif signal == "yellow":
    print("\n🟡 YELLOW SIGNAL")
   
    for i in range(5, 0, -1):
        print("Timer:", i, "seconds")
        time.sleep(1)
        print("SLOW DOWN")
elif signal == "green":
    print("\n🟢 GREEN SIGNAL")
    
    
    for i in range(5, 0, -1):
        print("Timer:", i, "seconds")
        time.sleep(1)

    print("GO")
else:
    print("❌ Invalid signal colour")

