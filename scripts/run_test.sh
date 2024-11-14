#!/bin/env bash
# **********************************************************************************
#                                                                                  *
# Author/s    : Luca Salvarani                                                     *
# Created on  : 2024-11-12 00:43:51                                                *
# Description :                                                                    *
#                                                                                  *
# **********************************************************************************


# From: 
#      https://vaneyckt.io/posts/safer_bash_scripts_with_set_euxo_pipefail/
#      https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html
set -o pipefail
set -o errtrace      # Same as `set -E`
set -o nounset       # Same as `set -u`
# set -o errexit     # Same as `set -e`, useful ONLY for short and simple scripts

declare -r DEFAULT_PORT_NUMBER=5;

main () {
    local action="" port_number=$DEFAULT_PORT_NUMBER;

    # From this excellent StackOverflow answer: https://stackoverflow.com/a/14203146/8965861
    OPTIND=1;
    POSITIONAL=();
    while [[ $# -gt 0 ]]; do
        case $1 in
            -n)
                port_number="${2:-$port_number}";
                shift 2;
            ;;
            -\? | -h |--help)
                show_usage
                return 0;
            ;;
            --)
                shift;
                while [[ $# -gt 0 ]]; do POSITIONAL+=("$1"); shift; done
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

    if [ $# -eq 0 ]; then
        show_usage >&2;
        exit 1;
    fi

    action="${1,,}";

    case "$action" in
        ports)
            for (( i=1; i<=port_number; i++ )); do
                # shellcheck disable=SC2016
                nohup bash -c "
                    while true; do
                        netcat -vvl -c 'read message; echo \"Received message: \$message\"';
                    done
                " > "/tmp/exercise_$action/port_$port_number.out" 2>&1 &
            done
            ;;
        *)
            echo "Invalid action: $1";
            exit 1;
            ;;
    esac

    return 0;
}

show_usage () {
    printf "Usage: %s [options] <action>\n" "$0";
    printf "\n";

    printf "Options:\n";
    printf "  -n <number>  Number of ports to open (default: %d)\n" "$DEFAULT_PORT_NUMBER";
    printf "  -h, --help   Show this help message\n";
    printf "\n";

    printf "Actions:\n";
    printf "  ports        Open a number of ports\n";
    printf "\n";
}

main "$@"