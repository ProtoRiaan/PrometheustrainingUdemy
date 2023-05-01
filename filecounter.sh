#!/bin/bash

DIR=/tmp

RESULT=$(ls ${DIR}/push-???? | wc -l)

END="$(date +%S)"

cat << EOF > "$DIR/pushfiles.prom.$$"
node_pushfiles_total $RESULT
node_pushfiles_last_run_seconds $END
EOF

mv "$DIR/pushfiles.prom.$$" \
"$DIR/pushfiles.prom"


