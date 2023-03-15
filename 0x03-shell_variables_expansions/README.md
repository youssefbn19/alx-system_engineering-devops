#  Shell, init files, variables and expansions Tasks
**task 0 :** alias ls="rm *" command creates an alias with a name ls and value rm *.<br/>
**task 1 :** echo "hello $USER".<br/>
**task 2 :** export PATH="$PATH:/action" command add action directory to the PATH variable to be clear this command only concat the previous path and add /action.<br/>
**task 3 :** echo $PATH | tr ":" "\n" | wc -l command counts the number of directories in the PATH.<br/>
**task 4 :** printenv command lists environment variables.<br/>
**task 5 :** set command lists all local variables and environment variables, and functions.<br/>
**task 6 :** BEST="School" command create a local variable named BEST with value School<br/>
**task 7 :** export BEST="School" command create a global variable named BEST with value School<br/>
**task 8 :** echo $(($TRUEKNOWLEDGE + 128)) command prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE<br/>
**task 9 :** echo $(($POWER/$DIVIDE)) command prints the result of POWER variable divided by DIVIDE variable<br/>
**task 10 :** echo $(($BREATH**$LOVE)) command displays the result of BREATH variable to the power LOVE variable<br/>
**task 12 :** echo -e {a..z}{a..z} | tr ' ' '\n' | grep -v 'oo' command print all possible combinations of two letters, and show each combination in seperate line expect oo combination won't be shown.<br/>
**task 13 :** printf "%.2f\n" $NUM command prints a number with two decimal places, followed by a new line.<br/>
