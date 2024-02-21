# incomplete code for students to complete
def is_ipv4(input: str) -> bool:
    # your code here
    return False


# tests
assert is_ipv4("192.168.1.1") is True
assert is_ipv4("255.255.255.255") is True
assert is_ipv4("256.100.50.25") is False
assert is_ipv4("lol.wut.no") is False
assert is_ipv4("192.168.1") is False
assert is_ipv4("192.168.01.1") is False
print("All tests passed - our hero can travel to the planet safely!")
