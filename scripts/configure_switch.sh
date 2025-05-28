#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

main () {
    local host port;

    local -a ssh_options=(
        -o KexAlgorithms=+diffie-hellman-group1-sha1
        -o HostKeyAlgorithms=+ssh-rsa
        -o StrictHostKeyChecking=no
        -o UserKnownHostsFile=/dev/null
    )

    # From this excellent StackOverflow answer: https://stackoverflow.com/a/14203146/8965861
    OPTIND=1;
    POSITIONAL=();
    while (( $# > 0 )); do
        case $1 in
            -\? | -h |--help)
                # Call to usage function goes here
                return 0;
            ;;
            --)
                shift;
                while (( $# > 0 )); do POSITIONAL+=("$1"); shift; done
                break;
            ;;
            -*)
                printf "ERROR: Unknown option '%s'" "$1" >&2;
                return 1;
            ;;
            *)
                POSITIONAL+=("$1");
                shift;
            ;;
        esac;
    done;
    [[ ${#POSITIONAL[@]} -gt 0 ]] && set -- "${POSITIONAL[@]}";

    host="${1:-}";
    port="${2:-}";

    if [[ -z "$host" || -z "$port" ]]; then
        printf "ERROR: Missing required arguments: host and port.\n" >&2;
        return 1;
    fi

    if [[ ! $port =~ ^[0-9]+$ || $port -lt 1 || $port -gt 65535 ]]; then
        printf "ERROR: Port must be a number between 1 and 65535.\n" >&2;
        return 1;
    fi

    ssh "$host" -p "$port" "${ssh_options[@]}" <<-EOF
        
	EOF
}


main "$@"