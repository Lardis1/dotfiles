#!/bin/bash

function python_venv() {
    echo -e "\n${VIRTUAL_ENV:+($(basename $VIRTUAL_ENV))─}"
}

function __col() {
    echo "%F{${1}}"
}

PRIM_1=$(__col '#7FA658')
PRIM_2=$(__col '#648C58')

SEC_1=$(__col '#A6904E')
SEC_2=$(__col '#A67246')

TIRT_1=$(__col '#A62E38')

# BLACK=$(__col '#262524')
WHITE=$(__col '#D9D9D9')

yB='%B'
nB='%b'

function git_branch_name() {
  branch=$(git symbolic-ref HEAD 2> /dev/null | awk 'BEGIN{FS="/"} {print $NF}')
  if [[ -z "$branch" ]];
  then
    :
  else
    echo "%B$PRIM_2($SEC_1$branch$PRIM_2) "
  fi
}

function get_dirs_prompt() {
    # extract base directory
    if [ ! -z "$(echo $PWD | grep ^$HOME)" ];
    then
        BASEDIR="$HOME"
        BDSTRING="$WHITE~"
        SECOND_LEVEL_DIR="$(echo $PWD | cut -d'/' -f1-4)"
        SECOND_LEVEL_STRING="$SEC_1$(echo $PWD | cut -d'/' -f4)"
        THIRD_LEVEL_DIR="$(echo $PWD | cut -d'/' -f1-5)"
        THIRD_LEVEL_STRING="$SEC_1$(echo $PWD | cut -d'/' -f5)"
    else
        BASEDIR="/$(echo $PWD | cut -d'/' -f2)"
        BDSTRING="$WHITE$(echo $PWD | cut -d'/' -f2)"
        SECOND_LEVEL_DIR="$(echo $PWD | cut -d'/' -f1-3)"
        SECOND_LEVEL_STRING=$SEC_1"$(echo $PWD | cut -d'/' -f3)"
        THIRD_LEVEL_DIR="$(echo $PWD | cut -d'/' -f1-4)"
        THIRD_LEVEL_STRING=$SEC_1"$(echo $PWD | cut -d'/' -f4)"
    fi

    if [ "$PWD" == "$BASEDIR" ];
    then
        echo "$SEC_2($BDSTRING$SEC_2)"
    elif [ "$PWD" == "$SECOND_LEVEL_DIR" ];
    then
        echo "$SEC_2($BDSTRING$SEC_2/$SECOND_LEVEL_STRING$SEC_2)"
    elif [ "$PWD" == "$THIRD_LEVEL_DIR" ];
    then
        echo "$SEC_2($BDSTRING$SEC_2/$SECOND_LEVEL_STRING$SEC_2/$THIRD_LEVEL_STRING$SEC_2)"
    else
        echo "$SEC_2($BDSTRING$SEC_2)─$SEC_2[$SEC_1%1~$SEC_2]"
    fi
}

LINE_1=$yB$TIRT_1$'\uf327 '$PRIM_1$'  %n'$PRIM_2$' in '"$(get_dirs_prompt)"'%b'
LINE_2="$(git_branch_name)$SEC_1❯$nB%F{reset} "
echo -e "$LINE_1\n$LINE_2"
