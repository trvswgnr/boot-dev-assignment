# complete solution
def is_ipv4(input: str) -> bool:
    """
    Check if the provided string is a valid IPv4 address.

    Args:
        input (str): The string to validate as an IPv4 address.

    Returns:
        bool: `True` if the string is a valid IPv4 address, `False` otherwise.
    """
    parts = input.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if not 0 <= int(part) <= 255:
            return False
        if part[0] == "0" and len(part) > 1:
            return False
    return True


# tests
assert is_ipv4("192.168.1.1") is True
assert is_ipv4("255.255.255.255") is True
assert is_ipv4("256.100.50.25") is False
assert is_ipv4("lol.wut.no") is False
assert is_ipv4("192.168.1") is False
assert is_ipv4("192.168.01.1") is False
print("All tests passed - our hero can travel to the planet safely!")
