import sys
import pytest

sys.path.insert(
    0,
    'src'
)

from http_headers_grabber.http_headers_grabber import HttpHeadersGrabber

@pytest.fixture
def http_headers_grabber_available():
    return HttpHeadersGrabber.http_headers_grabber('https://google.com')

@pytest.fixture
def http_headers_grabber_witout_preffix():
    return HttpHeadersGrabber.http_headers_grabber('google.com')

def test_http_headers_grabber_available(http_headers_grabber_available):
    assert dict(http_headers_grabber_available)['X-Frame-Options'] == 'SAMEORIGIN'
    assert dict(http_headers_grabber_available)['Content-Encoding'] == 'gzip'

def test_http_headers_grabber_witout_preffix(http_headers_grabber_witout_preffix):
    assert dict(http_headers_grabber_witout_preffix)['X-Frame-Options'] == 'SAMEORIGIN'
    assert dict(http_headers_grabber_witout_preffix)['Content-Encoding'] == 'gzip'

def test_http_headers_grabber_invalid_url_type():
    try:
        return HttpHeadersGrabber.http_headers_grabber(123)
    except BaseException as ex:
        assert str(ex) == 'Target must be a string not <class \'int\'>. Got target: 123'
