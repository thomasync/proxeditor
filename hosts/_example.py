import mitmproxy
import json
from tldextract import extract
import logging

HOSTS = [
    'example.fr',
    'example.org'
]

SCRIPT = """
<script>
    window.addEventListener('load', function() {
        document.querySelector('#username').value = 'user';
        document.querySelector('#password').value = 'password';
        document.querySelector('#login').click();
    });
</script>
"""

STYLE = """
<style>
    html, body {
        background-color: yellow !important;
    }
</style>
"""

class Example:

    # Give access to the request
    @staticmethod
    def tls_clienthello(data: mitmproxy.proxy.layers.tls.ClientHelloData) -> None:
        domain = extract(data.context.server.address[0]).registered_domain
        if domain in HOSTS:
            data.ignore_connection = False

    # Event called when a request is sent
    @staticmethod
    def request(flow: mitmproxy.http.HTTPFlow) -> None:
        domain = extract(flow.request.host).registered_domain
        if domain not in HOSTS:
            return
            
        if "verify_premium" in flow.request.path:
            flow.kill()
            logging.error("example debug message")

    # Event called when a response is received
    @staticmethod
    def response(flow: mitmproxy.http.HTTPFlow) -> None:
        domain = extract(flow.request.host).registered_domain        
        if domain not in HOSTS or flow.response.content == '':
            return

        if "article" in flow.request.path:
            response = json.loads(flow.response.content)
            response["response"]["article"]["unlocked"] = "1"
            flow.response.content = json.dumps(response).encode()

        elif "user" in flow.request.path:
            response = json.loads(flow.response.content)
            response["response"]["user"]["category"] = "premium"
            response["response"]["user"]["subscription"]["isPremium"] = "true"
            flow.response.content = json.dumps(response).encode()
        
        elif "login" in flow.request.path:
            flow.response.content += (STYLE + SCRIPT).encode();
