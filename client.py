from config import STUBS, PROTOS
from flask import Flask, request
from google.protobuf.json_format import MessageToJson
from grpc import insecure_channel

app = Flask(__name__)


@app.route('/grpc_request', methods=['POST'])
def grpc_request():
    res, err = None, None
    dct = {}
    if request.method == 'POST':
        try:
            # init data
            data = request.get_json()
            for arg in ['cmd', 'proto', 'server']:
                val = request.args.get(arg)
                if not val:
                    return f'{{"error": {arg} not specified in uri, "response": {res}}}'
                else:
                    dct[arg] = val
            # grpc request
            with insecure_channel(dct['server'], options=(('grpc.enable_http_proxy', 0),)) as channel:
                stub_func = STUBS.get_stub_func(channel, dct['cmd'].split('.'))
                proto_class = PROTOS.get_collection().get(dct['proto'], None)
                if not stub_func:
                    err = f'unable to load stub func with {dct["cmd"]}'
                elif not proto_class:
                    err = f'unable to load proto class with {dct["proto"]}'
                else:
                    if data:
                        res = MessageToJson(stub_func(proto_class(**data)))
                    else:
                        res = MessageToJson(stub_func(proto_class(None)))
        except Exception as e:
            err = e
    else:
        err = 'only POST method is supported'
    return f'{{"error": {err}, "response": {res}}}'
