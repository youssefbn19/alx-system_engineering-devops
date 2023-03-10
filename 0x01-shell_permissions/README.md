# Task Shell Permissions Command
Task 0: su betty command switches the current user to the user betty.<br/>
Task 1: id –nu command prints the effective usernane of the current user.<br/>
Task 2: id –nG command prints prints all the groups of the current user.<br/>
Task 3: chown betty hello comand changes the owner of the file hello to the user betty
Task 4: touch hello command creates an empty file called hello.
Task 5: chmod u+x hello command adds execute permission to the owner of the file hello 
Task 6: chmod ug+x,o+r hello command adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
Task 7: chmod ugo+x hello command adds execution permission to the owner, the group owner and the other users, to the file hello
Task 8: chmod 007 hello command gives no permissions to Owner nor Group and give all permissions to Other users.
Task 9: chmod 753 hello command give all permissions to Owner, read and execute to group, write and execute to the Others.
Task 10:  chmod --reference=olleh hello command sets the mode of the file hello the same as olleh’s mode
Task 11: chmod ugo+x */ command adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users.
Task 12: mkdir my_dir -m 751 command Create a script that creates a directory called my_dir with permissions 751 in the working directory
Task 13: chown :school file command changes the group owner to school for the file hello

