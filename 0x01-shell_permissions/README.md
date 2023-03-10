# Task Shell Permissions Command
Task 0: su betty command switches the current user to the user betty.<br/>
Task 1: id –nu command prints the effective usernane of the current user.<br/>
Task 2: id –nG command prints prints all the groups of the current user.<br/>
Task 3: chown betty hello comand changes the owner of the file hello to the user betty.<br/>
Task 4: touch hello command creates an empty file called hello.<br/>
Task 5: chmod u+x hello command adds execute permission to the owner of the file hello.<br/>
Task 6: chmod ug+x,o+r hello command adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.<br/>
Task 7: chmod ugo+x hello command adds execution permission to the owner, the group owner and the other users, to the file hello<br/>
Task 8: chmod 007 hello command gives no permissions to Owner nor Group and give all permissions to Other users.<br/>
Task 9: chmod 753 hello command give all permissions to Owner, read and execute to group, write and execute to the Others.<br/>
Task 10:  chmod --reference=olleh hello command sets the mode of the file hello the same as olleh’s mode.<br/>
Task 11: chmod ugo+x */ command adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users.<br/>
Task 12: mkdir my_dir -m 751 command Create a script that creates a directory called my_dir with permissions 751 in the working directory.<br/>
Task 13: chown :school file command changes the group owner to school for the file hello.<br/>
Task 14: chown vincent:staff * command changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.<br/>
Task 15: chown vincent:staff -h _hello command changes the owner and the group owner of symbolic link  _hello to vincent and staff respectively.<br/>
Task 16: chown --from=guillaume betty hello command changes the owner of the file hello to betty only if it is owned by the user guillaume.<br/>
Task 17: telnet towel.blinkenlights.nl command play the StarWars IV episode in the terminal.<br/>
