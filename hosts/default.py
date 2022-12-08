import mitmproxy
from tldextract import extract
import logging 


HOSTS_ADS = ['googleadservices.com', 'taboola.com', 'batch.com', 'googlesyndication.com', 'doubleclick.net', 'xiti.com']

class Default:

    @staticmethod
    def tls_clienthello(data: mitmproxy.proxy.layers.tls.ClientHelloData) -> None:
        domain = extract(data.context.server.address[0]).registered_domain
        
        if domain in HOSTS_ADS:
            data.ignore_connection = False
        else:
            # Set to false for debug
            data.ignore_connection = False

    @staticmethod
    def request(flow: mitmproxy.http.HTTPFlow) -> None:
        for host in HOSTS_ADS:
            domain = extract(flow.request.host).registered_domain
            if host in domain:
                flow.kill()
