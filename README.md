# grpc-http-proxy
This project serves as a proxy between grpc and http. 

## Installation
1. Git clone this repo.

2. Create a virtual environment in the root folder of the git repo.<br/>
**Note**: ```pip install virtualenv``` if ```pip freeze|grep virtualenv``` returns empty.
    ```sh
    # For Python 2
    virtualenv venv
   
    # For Python 3
    python3 -m venv venv
    ```
   
3. Install project dependencies via requirements.txt.
    ```sh
    # For Python 2
    pip install -r requirements.txt
   
    # For Python 3
    pip3 install -r requirements.txt
    ```
## Makefile
There are 4 targets in the make file. The default goal is download-compile-run.
These targets rely on config.sh for exported variables, which can be overwritten via environment variables.

| target               | desc                                   | command             |
|----------------------|----------------------------------------|---------------------|
| download-proto       | downloads the proto from srec_dd_basis | make download-proto |
| compile-proto        | compiles the proto in the proto folder | make compile-proto  |
| run                  | runs the flask client                  | make run            |
 | download-compile-run | default target                         | make                |

   
## How to construct the curl request
1. The curl statement comprises the following component.
   ``` sh
   curl -L -X POST 'http://<local_server>/grpc_request?cmd=<stub_class>.<attr_name>&proto=<request_proto>&server=<remote_server>' \
   -H 'content-type: application/json' \
   --data-raw '<json_data>'
   ```
   1. **local_proxy_server**: ip address of this application
   2. **stub_class**: the name of the stub class found in _pb2_grpc.py
   3. **attr_name**: the attribute name belonging to the stub class
   4. **proto**: the proto request found in _pb2.py
   5. **remote_server**: ip address of the remote brpc/grpc server

2. A sample curl is provided below.
   ``` sh
   curl -L -X POST 'http://127.0.0.1:5000/grpc_request?cmd=RecallServiceStub.MBPGetRecallItems&proto=RcmdReq&server=10.168.131.216:37741' \
   -H 'content-type: application/json' \
   --data-raw '{"Userid":1}'
   ```
