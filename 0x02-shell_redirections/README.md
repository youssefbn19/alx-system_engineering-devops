# I/O Redirection Tasks
**Task 0** : echo Hello, World command prints “Hello, World”.<br/>
**Task 1** : echo "\"(Ôo)'" command displays a confused smiley "(Ôo)'.<br/>
**Task 2** : cat /etc/passwd command displays passwd file content.<br/>
**Task 3** : cat /etc/passwd /etc/hosts command displays passwd and hosts content.<br/>
**Task 4** : tail /etc/passwd command displays the last 10 lines of passwd file.<br/>
**Task 5** : head /etc/passwd command displays the first 10 lines of passwd file.<br/>
**Task 6** : head -n 3 iacta | tail -n 1 command displays the third line of the file iacta.<br/>
**Task 7** : echo Best School > "\*\\\'\"Best School\"\'\\\*$\?\*\*\*\*\*:)" command creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School.<br/>
**Task 8** : ls -la > ls_cwd_content command writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.<br/>
**Task 9** : tail -n 1 iacta >> iacta command duplicates the last line of the file iacta.<br/>
**Task 10** : find -type f -name "*.js" -delete command deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.<br/>
**Task 11** : find . -mindepth 1  -type d | wc -l command counts the number of directories and sub-directories in the current directory.<br/>
**Task 12** : ls -t | head command displays the 10 newest files in the current directory.<br/>
**Task 13** : sort | uniq -u command takes a list of words as input and prints only words that appear exactly once.<br/>
**Task 14** : grep root /etc/passwd command displays lines containing the pattern “root” from the file /etc/passwd.<br/>
**Task 15** : grep bin /etc/passwd | wc -l command displays the number of lines that contain the pattern “bin” in the file /etc/passwd.<br/>
**Task 16** : grep root /etc/passwd -A 3 command displays lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.<br/>
**Task 17** : grep bin -v /etc/passwd command displays all the lines in the file /etc/passwd that do not contain the pattern “bin”.<br/>
**Task 18** : grep '^[a-zA-Z]' /etc/ssh/sshd_config command displays all lines of the file /etc/ssh/sshd_config starting with a letter.<br/>
**Task 19** : tr Ac Ze command Replace all characters A and c from input to Z and e respectively.<br/>
**Task 20** : tr -d Cc command removes all letters c and C from input.<br/>
**Task 21** : rv command reverse its input.<br/>
**Task 22** : cut -d ":" -f 1,6 /etc/passwd | sort command displays all users and their home directories, sorted by users based on the /etc/passwd file.<br/>
