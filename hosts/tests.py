import mitmproxy
from tldextract import extract
import logging
import re

HOSTS = [
    'neverssl.com',
    'github.com'
]

PAGE = """
<html lang="fr">
    <head>
        <title>Proxy Works</title>
    </head>
    <body>
        <h1>Proxy Works</h1>
    </body>
</html>
"""

class Tests:

    # Give access to the request
    @staticmethod
    def tls_clienthello(data: mitmproxy.proxy.layers.tls.ClientHelloData) -> None:
        domain = extract(data.context.server.address[0]).registered_domain
        if domain in HOSTS:
            data.ignore_connection = False

    # Event called when a response is received
    @staticmethod
    def response(flow: mitmproxy.http.HTTPFlow) -> None:
        domain = extract(flow.request.host).registered_domain        

        if domain not in HOSTS or "proxeditor_pytest" not in flow.request.path:
            return

        logging.error("Domain: " + domain)

        if "neverssl.com" == domain and "online/create" in flow.request.path:
            flow.response.status_code = 200
            flow.response.content = PAGE.encode()
        
        elif "neverssl.com" == domain and "online" in flow.request.path:
            flow.response.content = flow.response.content.replace(b'42C0FD', b'43b045')
        
        elif "neverssl.com" == domain and "redirect" in flow.request.path:
            flow.response.status_code = 302
            flow.response.headers['Location'] = 'https://neverssl.com/online/'

        elif "github.com"== domain and "thomasync" in flow.request.path:
            content = flow.response.content.decode()
            content = re.sub(r'<title>(.*?)</title>', r'<title>\1 (Proxy Works!)</title>', content, 0, re.DOTALL)
            flow.response.content = content.encode()
            