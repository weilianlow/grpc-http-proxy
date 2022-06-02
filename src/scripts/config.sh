# get proto
export GIT_REPO_PROTO=${GIT_REPO_PROTO:="git@github.com:protocolbuffers/protobuf.git"}
export PROTO_BASE_FOLDER=${PROTO_BASE_FOLDER:="proto"}
export BRANCH=${BRANCH:="master"}
# protoc
export PROTO_SRC_FOLDER=${PROTO_SRC_FOLDER:="$PROTO_BASE_FOLDER/srec_protos"}
export PROTO_GEN_FOLDER=${PROTO_GEN_FOLDER:="$PROTO_BASE_FOLDER/gen"}
# flask
export FLASK_APP=${FLASK_APP:="client"}
export FLASK_ENV=${FLASK_ENV:="development"}
export FLASK_HOST=${FLASK_HOST:="127.0.0.1"}
export FLASK_PORT=${FLASK_PORT:="5000"}
export PYTHONPATH=$PYTHONPATH:"$PROTO_GEN_FOLDER"
