source config.sh
rm -rf "$PROTO_BASE_FOLDER"
mkdir "$PROTO_BASE_FOLDER"
cd "$PROTO_BASE_FOLDER"
git clone -b "$BRANCH" "$GIT_REPO_PROTO" || exit 1
