import sys
import socket
import pytest

sys.path.insert(
    0,
    'src'
)

from ip.ip import GetHostname

@pytest.fixture
def get_hostname():
    return GetHostname.get_hostname_ip()

def test_get_hostname(get_hostname):
    hostname, _ = get_hostname
    assert hostname == socket.gethostname()
