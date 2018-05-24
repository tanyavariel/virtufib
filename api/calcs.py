from flask import make_response
JSON_MIME_TYPE = application/json
def genfbseq(seqnum):
    ra = 0
    rb = 1
    fibs = []
    if seqnum <= 0:
        return -1
    if seqnum == 1:
        return 0
    if seqnum == 2:
        return 1
    while (seqnum):  ## seqnum -1 because we want the fib just before the one at the seqnum place - no do while loop unfort
        rs  =  ra + rb 
        fibs.append(ra)
        ra  =  rb
        rb  =  rs
        seqnum -= 1
        
    return fibs
def json_response(data=, status=200, headers=None):
    headers = headers or {}
    if Content-Type not in headers:
        headers[Content-Type] = JSON_MIME_TYPE
    return make_response(data, status, headers)
