# Constant system logging profile
logging_profile = ("192.168.1.100", 8080)

# Unpack the tuple
ip_address, server_port = logging_profile

print("===== System Logging Profile =====")
print("IP Address:", ip_address)
print("Server Port:", server_port)

# Attempt to modify the tuple
try:
    logging_profile[0] = "10.0.0.1"
except TypeError:
    print("Modification failed: Logging profile is immutable.")

print("Final Logging Profile:", logging_profile)
