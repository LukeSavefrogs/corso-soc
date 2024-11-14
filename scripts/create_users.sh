#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

main () {
    # Create the needed users in the following format:
    # username,lastname,firstname

    while read -ru3 line; do
        local student=()

        # Skip header or empty lines
        if [[ "$line" =~ ^(\ *username,lastname,firstname\ *| *)$ ]]; then
            continue
        fi

        IFS=',' read -r -a student <<< "$line"

        useradd "${student[0]}" \
            --create-home \
            --groups students,sudo \
            --comment "${student[2]} ${student[1]}" \
            --home-dir "/home/${student[0]}" \
            --shell /bin/bash \
        && echo -n "${student[0]}:${student[0]}" | chpasswd
    done 3< "$1"
}


main "$@"