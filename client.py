import json

from config import STUBS, PROTOS, COMMANDS_DUMP, PROTOS_DUMP
from flask import Flask, request
from google.protobuf.json_format import MessageToJson
from grpc import insecure_channel

app = Flask(__name__)


@app.route('/get_commands', methods=['GET'])
def get_commands():
    global COMMANDS_DUMP
    if not COMMANDS_DUMP:
        lst = []
        dct = STUBS.get_collection()
        c = insecure_channel(target='')
        for key in dct:
            if key.lower().endswith('stub'):
                instance = dct[key](c)
                for val in instance.__dict__:
                    lst.append(f'{key}.{val}')
        COMMANDS_DUMP = json.dumps(lst)
    return f'{{"commands": {COMMANDS_DUMP}}}'


@app.route('/get_protos', methods=['GET'])
def get_protos():
    global PROTOS_DUMP
    if not COMMANDS_DUMP:
        lst = [key for key in PROTOS.get_collection()]
        PROTOS_DUMP = json.dumps(lst)
    return f'{{"protos": {PROTOS_DUMP}}}'


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
                chan_unary = STUBS.get_channel_unary(channel, dct['cmd'].split('.'))
                proto_class = PROTOS.get_collection().get(dct['proto'], None)
                if not chan_unary:
                    err = f'unable to load stub func with {dct["cmd"]}'
                elif not proto_class:
                    err = f'unable to load proto class with {dct["proto"]}'
                else:
                    if data:
                        res = MessageToJson(chan_unary(proto_class(**data)))
                    else:
                        res = MessageToJson(chan_unary(proto_class(None)))
        except Exception as e:
            err = e
    else:
        err = 'only POST method is supported'
    return f'{{"error": {err}, "response": {res}}}'
