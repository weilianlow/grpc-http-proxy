.DEFAULT_GOAL := all
SHELL := /bin/bash

download-proto:
	@sh src/scripts/download_proto.sh

compile-proto:
	@sh src/scripts/compile_proto.sh

run-client:
	@sh src/scripts/client.sh

all: download-proto compile-proto run-client

compile-sample-proto:
	#rm -rf "proto/gen"
	#mkdir "proto/gen"
	python -m grpc_tools.protoc -I "." --python_out="proto/gen" --grpc_python_out="proto/gen" src/sample/helloworld.proto

run-server:
	@sh src/scripts/server.sh