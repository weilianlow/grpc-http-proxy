.DEFAULT_GOAL := all

download-proto:
	@sh download_proto.sh

compile-proto:
	@sh compile_proto.sh

run-client:
	@sh client.sh

all: download-proto compile-proto run-client

compile-sample-proto:
	rm -rf "proto/gen"
	mkdir "proto/gen"
	python -m grpc_tools.protoc -I "." --python_out="proto/gen" --grpc_python_out="proto/gen" helloworld.proto

run-server:
	@sh server.sh