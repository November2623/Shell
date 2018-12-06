_MAIN STRUCTURE_
Special case:
    1. . file => '.' dot is a bultin of main shell
    2. '=' => treat as variable

Usual Case:
    1. PATH

    menu.bash
    check.sh
    shell.py
    => "name" command not found => IT IS NOT KNOWN AS A PATH => bUILTIN

    ./menu.bash => denied
    ./check.sh => denied
    ./shell.py => denied
    => check permission

    . menu.bash => success
    . check.sh => success
    . shell.py => error
    => run as a binary file

    . cd => go home
    D*/ => bash: Desktop/: Is a directory
    D* => Desktop: command not found
    ls D* => out put file start by "D"


    2. COMMAND-NAME [ARGUMENTS]
    ls
    cd /
    cd //
    touch file{1,2,3}
    rm file{1,2,3}



-------------------------------------------------------------------------------
_FEATURE 1: GLOBBING_






-------------------------------------------------------------------------------
_FEATURE 2: PATH EXPANSION_

###
*TIDLE EXPANSION*
      1. ~
      2. ~+
      3. ~-
      4. ~+/dnhu/file => file has permission or not found
      5. ~-/dnhu => is a directory or nope
      6. unset "OLDPWD" => ~-: command not found
      7. ~+[number]: *~+4* => not yet
      8. ~-[number]: *~-2* => not yet
      9. ~sgdgedtghergsfgwe



###
*PARAMETER EXPANSION*
      1. a=scd qevqe qe qe => qevqe: command not found, ko luu bien a luon
      2. $a $abc => ket qya cua 'a'
      3. $a$abc => ket qua cua 'a' + 'abc'




-------------------------------------------------------------------------------
_FEATURE 11: COMMAND HISTORY AND "!"- EXECUTE COMMAND HISTORY BE CALLED_
        1. ! => don't do anything






###########################
1. check external file => open path
2. check bUILTIN => create a list contains name-builtin
