source "$(pwd)/src/scripts/config.sh"
flask run -h "$FLASK_HOST" -p "$FLASK_PORT" || exit 1