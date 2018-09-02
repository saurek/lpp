import fcntl
import os
import socket


def get_ip(inter):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip_addr = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256', inter[:15]))[20:24])
    return ip_addr


def get_mac_address(inter):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', inter[:15]))
    mac_address = ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]
    return mac_address