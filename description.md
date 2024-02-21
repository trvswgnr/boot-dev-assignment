# What is an IP Address?

An IP address is a unique identifier for a device on a network. Imagine the internet as a massive, sprawling city. Each device connected to the internet is like a house in this city. Just like every house has a mailing address, every device has something known as an [**IP address**](https://developer.mozilla.org/en-US/docs/Glossary/IP_Address). We can use this address to send information from one device to another over the internet. It can also be used to determine the general location of a device, if you're into that sort of thing.

There are two versions of IP (Internet Protocol) addresses:

- **IPv4**: This is the most common form. It consists of four numbers separated by dots, e.g., `192.168.1.1`. Each number can range from `0` to `255`.
- **IPv6**: This is the newer, fancier version that was developed to deal with the shortage of available IPv4 addresses. It consists of eight groups of four hexadecimal digits, e.g., `2001:0db8:85a3:0000:0000:8a2e:0370:7334`.

## Assignment

Our game is vast and has many different worlds that can be travelled to by knowing the IP address. Our hero is brave enough to venture out and explore the planet Eberron, but without a valid IP address, they could be lost forever! Your task is to write a Python function that checks if the string our hero entered is a valid IPv4 address. The function should return `True` if the input is a valid IPv4 address and `False` otherwise.

Here are the rules for a valid IPv4 address:

1. It must have exactly four numbers.
2. Each number is between `0` and `255`.
3. There are no leading zeros in any of the numbers.

Example of valid IPv4 addresses: `192.168.1.1`, `255.255.255.255`
Example of invalid IPv4 addresses: `lol.wut.no`, `192.168.1`, `192.168.01.1`

**Hint**: You might find the `split()` method and `isdigit()` function useful.
