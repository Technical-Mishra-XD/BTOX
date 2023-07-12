# Dont Edit any code Of modify File Its baba programmer
# Hatters Just feel you :)
import hashlib
import hmac
import requests
import os


class FacebookSession(object):

    GRAPH = 'https://graph.facebook.com'

    def __init__(self, app_id=None, app_secret=None, access_token=None,
                 proxies=None, timeout=None, debug=False):

        self.app_id = app_id
        self.app_secret = app_secret
        self.access_token = access_token
        self.proxies = proxies
        self.timeout = timeout
        self.debug = debug
        self.requests = requests.Session()
        self.requests.verify = os.path.join(
            os.path.dirname(__file__),
            'fb_ca_chain_bundle.crt',
        )
        params = {
            'access_token': self.access_token
        }
        if app_secret:
            params['appsecret_proof'] = self._gen_appsecret_proof()
        self.requests.params.update(params)

        if self.proxies:
            self.requests.proxies.update(self.proxies)

    def _gen_appsecret_proof(self):
        h = hmac.new(
            self.app_secret.encode('utf-8'),
            msg=self.access_token.encode('utf-8'),
            digestmod=hashlib.sha256
        )

        self.appsecret_proof = h.hexdigest()
        return self.appsecret_proof

__all__ = ['FacebookSession']
