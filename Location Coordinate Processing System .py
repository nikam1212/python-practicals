# Store GPS coordinates in a tuple
location = (18.5204, 73.8567)

print("GPS Location:", location)

# Indexing
print("Latitude:", location[0])
print("Longitude:", location[1])

# Tuple operations
print("Number of coordinates:", len(location))

# Access first element using negative indexing
print("First coordinate:", location[0])

# Access last element using negative indexing
print("Last coordinate:", location[-1])

# Check whether a coordinate exists
print("Is latitude 18.5204 present?", 18.5204 in location)

# Tuple slicing
print("Coordinates using slicing:", location[0:2])

# Concatenation
extra = ("Dubai",)
new_location = location + extra

print("Location with city:", new_location)

# Repetition
print("Repeated coordinates:", location * 2)