import os
import sys

from utils import ProtoClassCollection

PROTO_ROOT = os.getenv('PROTO_GEN_FOLDER')
if not PROTO_ROOT:
    print('PROTO_GEN_FOLDER variable is not defined, terminating program.')
    sys.exit()
STUBS = ProtoClassCollection(PROTO_ROOT, '_pb2_grpc.py')
PROTOS = ProtoClassCollection(PROTO_ROOT, '_pb2.py')
COMMANDS_DUMP = None
PROTOS_DUMP = None