source "$(pwd)/src/scripts/config.sh"
rm -rf "$PROTO_GEN_FOLDER"
mkdir "$PROTO_GEN_FOLDER"
python -m grpc_tools.protoc -I "$PROTO_SRC_FOLDER" --python_out="$PROTO_GEN_FOLDER" --grpc_python_out="$PROTO_GEN_FOLDER" $(find "$PROTO_SRC_FOLDER" -iname "*.proto") || exit 1
