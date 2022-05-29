# grpc-http-proxy
This project serves as a proxy between grpc and http. 
![](src/img/proxy.png)

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
There are 6 targets in the make file. The default goal is download-compile-run.
These targets rely on config.sh for exported variables, which can be overwritten via environment variables.

| **target**             | **desc**                                | **command**               |
|------------------------|-----------------------------------------|---------------------------|
| download-proto         | downloads the proto from srec_dd_basis  | make download-proto       |
| compile-proto          | compiles the proto in the proto folder  | make compile-proto        |
| run-client             | runs the flask client                   | make run-client           |
| download-compile-run   | default target                          | make                      |
| compile-sample-proto   | compiles the sample proto               | make compile-sample-proto |
| run-server             | run the sample server                   | make run-server           |

   
## Commands
   ### POST /grpc_request
   Performs gRPC request to remote server and returns as json response
   #### Param definition
   ``` sh
   curl -X POST 'http://<local_server>/grpc_request?cmd=<stub_class>.<attr_name>&proto=<request_proto>&server=<remote_server>' \
   -H 'content-type: application/json' \
   -d '<json_data>'
   ``` 
   | **component**  | **desc**                                               |
   |----------------|--------------------------------------------------------|
   | proxy_server   | ip address of flask client (localhost if curl locally) |
   | stub_class     | the name of the stub class found in _pb2_grpc.py       |
   | attr_name      | the attribute name belonging to the stub class         |
   | proto          | the proto request found in _pb2.py                     |
   | remote_server  | ip address of brpc/grpc server                         |

   #### Sample cURL
   1. ItemServiceStub.GetItems (Requires vpn via sshuttle)
   ``` sh
   curl -X POST 'localhost:5000/grpc_request?cmd=ItemServiceStub.GetItems&proto=RcmdReq&server=127.0.0.1:5005' \
   -H 'content-type: application/json' \
   -d '{"Userid":1}'
   ```
   2. GreeterStub.SayHello (Requires to make compile-sample-proto, run flask client and sample server)
   ``` sh
   curl -X POST 'localhost:5000/grpc_request?cmd=GreeterStub.SayHello&proto=HelloRequest&server=localhost:50051' \
   -H 'content-type: application/json' \
   -d '{"name":"Peter", "age": 28, "contact":[{"email": "peter.ho@shopee.com"}, {"phone": "91234567"}]}'
   ```
   ### GET /get_commands
   Returns all commands compiled under _pb2_grpc.py
   #### Sample cURL
   ``` sh
   curl -X GET 'localhost:5000/get_commands'
   ```
   

   ### GET /get_protos
   Returns all proto classes compiled under _pb2.py
   #### Sample cURL
   ``` sh
   curl -X GET 'localhost:5000/get_protos'
   ```
