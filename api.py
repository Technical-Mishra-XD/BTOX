# -*- coding: utf-8 -*-    
# Don't modify any code its baba programmer


from . import sessions
def request(method, url, **kwargs):
    with sessions.Session() as session:
def        return session.request(method=method, url=url, **kwargs)def get(url, params=None, **kwargs):
    kwargs.setdefault('allow_redirects', True)
    return request('get', url, params=params, **kwargs)
def options(url, **kwargs):
    kwargs.setdefault('allow_redirects', True)
    return request('options', url, **kwargs)
def head(url, **kwargs):
    kwargs.setdefault('allow_redirects', False)
    return request('head', url, **kwargs)
def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)
def put(url, data=None, **kwargs):
    return request('put', url, data=data, **kwargs)
def patch(url, data=None, **kwargs):
    return request('patch', url, data=data, **kwargs)
def delete(url, **kwargs):
    return request('delete', url, **kwargs)





