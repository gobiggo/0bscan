#!/usr/bin/env python
# Can import any built-in Python Library
import urllib.parse
def assign(service, arg):
    if service != "www":
        return
    arr = urllib.parse.urlparse(arg)
    return True, '%s://%s/inc/conn_db.inc' % (arr.scheme, arr.netloc)

def audit(arg):
    code, head, res, errcode, final_url = curl.curl(arg)
    if code == 200 and 'db_id' in res and  'db_name' in res and 'db_pass' in res:
         security_warning(arg)


if __name__ == '__main__':

    audit(assign('www', 'http://61.77.63.86/')[1])