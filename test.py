from lxml import etree
from zeep.wsse import BinarySignature

body_bytes = open('./body.xml', 'rb').read()
envelope = etree.fromstring(body_bytes)
binary_signature = BinarySignature('./key.pem', './cert.pem')
envelope, soap_headers = binary_signature.apply(envelope, {})
signed_body_bytes = etree.tostring(envelope)
