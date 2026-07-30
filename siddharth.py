# Traffic Signal Simulator using Nested If

print("===== Traffic Signal Simulator =====")
print("1. Red")
print("2. Yellow")
print("3. Green")

signal = int(input("Enter signal number (1-3): "))

if signal == 1:
    emergency = input("Is there an emergency vehicle? (yes/no): ")

    if emergency.lower() == "yes":
        print("🚑 Allow emergency vehicle to pass.")
    else:
        print("🔴 STOP! Wait for the green signal.")

elif signal == 2:
    ready = input("Are you close to the signal? (yes/no): ")

    if ready.lower() == "yes":
        print("🟡 Slow down and prepare to stop.")
    else:
        print("🟡 Wait until the signal changes.")

elif signal == 3:
    seatbelt = input("Are you wearing a seatbelt? (yes/no): ")

    if seatbelt.lower() == "yes":
        print("🟢 GO! Drive safely.")
    else:
        print("🟢 Wear your seatbelt first, then drive.")

else:
    print("❌ Invalid signal number!")