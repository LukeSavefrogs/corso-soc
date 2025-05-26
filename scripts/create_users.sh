#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

main () {
    # Create the needed users in the following format:
    # username,lastname,firstname,students|teachers

    local input_file="${1:-}"
    if [[ -z "$input_file" ]]; then
        echo "Usage: $0 <input_file>" >&2
        return 1
    fi
    
    while read -ru3 line; do
        local username="" lastname="" firstname="" usertype=""

        # Skip header or empty lines
        if [[ "$line" =~ ^(\ *username,lastname,firstname,role\ *| *)$ ]]; then
            continue
        fi

        IFS=',' read -r username lastname firstname usertype <<< "$line"

        if [[ -z "$username" || -z "$lastname" || -z "$firstname" || -z "$usertype" ]]; then
            echo "ERROR: Invalid line '$line'" >&2
            return 1
        fi

        echo "INFO: Creating user $username with role $usertype (home=/home/${username})..."
        useradd "${username}" \
            --create-home \
            --groups ${usertype:-student}s,sudo \
            --comment "${firstname} ${lastname}" \
            --home-dir "/home/${username}" \
            --shell /bin/bash \
        && echo -n "${username}:${username}" | chpasswd
    done 3< <(tr -d '\r' < "$input_file"; printf '\n')

    echo "INFO: All users created successfully!"
}


main "$@"