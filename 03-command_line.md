# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > pwd - show current working directory path  
> > mkdir dirname- creating a directory  
> > rm -r dirname - deleting a directory  
> > touch filename - creating a file  
> > rm filename - deleting a file  
> > mv oldfilename newfilename - renaming a file  
> > ls -a - listing hidden files  
> > cp dirname/filename dirname/ - copying a file from one directory to another  
> > ls - list all files and directories in the working directory  
> > cd - change directory  
> > ls -l - lists all contents of a directory in long format  
> > mv filename dirname/ - moves file into directory  

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > ls - list all files and directories in the working directory.  
> > ls -a - list all hidden files in working directory.  
> > ls -l - lists all contents of working directory in long format.  
> > ls -lh - lists all contents of working directory in long format and in alphabetical order by file extension.  
> > ls -lah - lists all hidden files of working directory in long format and in alphabetical order by file extension.  
> > ls -t - lists all contents of working directory ordered by the time they were last modified.  
> > ls - Glp - lists all contents of working directory in long format excluding columns containing Group information and marking directories with a / sign.  

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -a, ls -l, ls -p, ls -R, ls-1

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > 'xargs' lets us build and execute command lines from standard input. 

> > E.g. find /tmp -name core -type f -print | xargs /bin/rm -f : Find files named core in or below the directory /tmp and delete them, processing filenames in such a way that file or directory names containing spaces or newlines are correctly handled.

 

