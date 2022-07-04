is_ready = True

if is_ready:
    state_msg = "Ready"
else:
    state_msg = "Not ready yet"
print(state_msg)

print()

is_ready = False

if is_ready:
    state_msg = "Ready"
else:
    state_msg = "Not ready yet"
print(state_msg)

print()

is_ready = True
state_msg = is_ready and "Ready" or "Not ready yet"
print(state_msg)

print()

is_ready = False
state_msg = is_ready and "Ready" or "Not ready yet"
print(state_msg)

print()

is_ready = True
state_msg = "Ready" if is_ready else "Not ready yet"
print(state_msg)

print()

is_ready = False
state_msg = "Ready" if is_ready else "Not ready yet"
print(state_msg)

print()

is_ready = True
print("Ready" if is_ready else "Not ready yet")

print()

is_ready = False
print("Ready" if is_ready else "Not ready yet")