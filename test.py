from lxml import etree
from zeep.wsse import BinarySignature

body_bytes = open('./body.xml', 'rb').read()
envelope = etree.fromstring(body_bytes)
binary_signature = BinarySignature('./key.pem', './cert.pem')
envelope, soap_headers = binary_signature.apply(envelope, {})
signed_body_bytes = etree.tostring(envelope)
"""
------------------------------------------------------------------------------------ OUTPUT BEGIN
Traceback (most recent call last):
  File "test.py", line 7, in <module>
    envelope, soap_headers = binary_signature.apply(envelope, {})
  File "/zeep-test/venv/lib/python3.8/site-packages/zeep/wsse/signature.py", line 104, in apply
    _sign_envelope_with_key_binary(
  File "/zeep-test/venv/lib/python3.8/site-packages/zeep/wsse/signature.py", line 287, in _sign_envelope_with_key_binary
    bintok.text = x509_data.find(QName(ns.DS, "X509Certificate")).text
AttributeError: 'NoneType' object has no attribute 'text'
------------------------------------------------------------------------------------ OUTPUT END
"""
