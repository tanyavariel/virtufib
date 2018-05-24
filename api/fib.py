import json
from flask import Flask, request, Response, abort, make_response
from flask_restful import Resource, Api
from .calcs import JSON_MIME_TYPE, genfbseq

app = Flask(__name__)
api = Api(app)

class fibhist:
    def __init__(self):
        fibreq = 0
        fibsn = 0
        fibresponse = ''

fibs = {}

reccnt = 0
mydebug = 0

class ReqHistory(Resource):
    def get(self):
        content = ''
        global fibs
        for fr in fibs:
            if mydebug: print ("fr[%s] fibs=[%s]" % (fr, fibs[fr].fibresponse))
            content = content + '<p> Request #| ' + str(fr) + ' | ' + ' Seq#:' + str(fibs[fr].fibsn) + ' | ' + str(fibs[fr].fibresponse) + '</p>'

        response = make_response(content, 200)
        response.headers['Content-type'] = 'text/html'
        return response

class NewReq(Resource):
    def get(self,fsnew):
        global reccnt
        if (fsnew.isdigit()): fsn = int(fsnew)
        else: fsn=0
        if fsn < 1:
            return make_response("Usage: Please use this syntax: /fib/# to return the fib sequence up to that sequence number", 200)
    
        fseq = genfbseq(fsn)
    
        # Add to our fib request history just for fun - of course this is only stored in me for now
        reccnt = reccnt + 1
        fibs[reccnt] = fibhist()  ## Instantiate another fibhist class for our array at reccnt
        fibs[reccnt].fibreq = reccnt
        fibs[reccnt].fibsn = fsn
        fibs[reccnt].fibresponse = str(json.dumps(fseq))
        if mydebug: print ("fseq [%d] reccnt=[%d] fibresponse=[%s]" % (fibs[reccnt].fibsn, reccnt, fibs[reccnt].fibresponse))
    
        content = json.dumps(fseq)
        return content, 200, {'Content-Type': JSON_MIME_TYPE}

class DelReq(Resource):
    def get(self,fib_seqn):
        if (fib_seqn.isdigit()): fsn = int(fib_seqn)
        else: fsn=0
        if fsn < 1:
            return make_response("Usage: To del an entry the is syntax: /defib/#", 200)
    
        if fibs.get(fsn):
            del fibs[fsn]
            content = "Seq record removed"
            return content, 200, {'Content-Type': JSON_MIME_TYPE}
        else:
            content = "Seq does not exist"
            return content, 200, {'Content-Type': JSON_MIME_TYPE}
            

@app.errorhandler(404)
def not_found(e):
    return '', 404

api.add_resource(ReqHistory, '/swfib/') #  hist
api.add_resource(NewReq, '/adfib/<fsnew>') # req fib
api.add_resource(DelReq, '/defib/<fib_seqn>')

