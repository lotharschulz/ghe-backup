#!/bin/bash
# http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail
IFS=$'\n\t'

usage="$(basename "$0") searchstring replacement file-to-replace-the-strings-into"

# $1 - string to replace
# $2 - replacement string
# $3 - file to replace the strings into

if [ "$1" == "-h" ] || [ "$1" == "--help" ] ; then
  echo "Usage: $usage"
  exit 0
fi

# Mac: use gnu-sed - brew install gnu-sed
# set the path in bash - PATH="/usr/local/opt/gnu-sed/libexec/gnubin:$PATH"
# http://daoyuan.li/a-normal-sed-on-mac/
if [ ! -z $1 ] && [ ! -z $2 ] && [ ! -z $3 ] ;
then
  sed -i "s;$1;$2;g" $3
fi
