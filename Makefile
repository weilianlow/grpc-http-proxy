.DEFAULT_GOAL := all

download-proto:
	@sh download_proto.sh

compile-proto:
	@sh compile_proto.sh

run:
	@sh run.sh

all: download-proto compile-proto run
