# Writeup: Linux Basics CTF Challenge

## Challenge Description

This challenge, titled "Linux Basics", is part of a Capture The Flag (CTF) competition. The goal is to answer a series of questions about Linux system administration and file properties to obtain the flag.

## Initial Access

The challenge is accessed via netcat:

```bash
nc challenge.ctf.games 30181
```

Upon connection, we're presented with a Linux shell and instructions to use the `answer` tool.

## Challenge Questions and Solutions

### Question 0: What's your home directory?

**Solution:** `/home/user`

**Method:** This can be determined by running `echo $HOME` or `pwd` if you're in the home directory when you connect.

### Question 1: Search the man pages. What command would you use to generate random permutations?

**Solution:** `shuf`

**Method:** Although `man -k "random permutation"` and `apropos "random permutation"` didn't return results, `shuf` is the standard Linux command for this purpose.

### Question 2: On what day was /home/user/myfile.txt modified?

**Solution:** `1997-08-29`

**Method:** We used the command:
```bash
stat -c %y /home/user/myfile.txt | cut -d ' ' -f1
```

### Question 3: How big is /home/user/myfile.txt, in kilobytes?

**Solution:** `22`

**Method:** We used the command:
```bash
ls -al  /home/user/myfile.txt 
```

### Question 4: What user owns the file /home/user/myfile.txt?

**Solution:** `root`

**Method:** We used the command:
```bash
stat -c %U /home/user/myfile.txt
```

### Question 5: What's the 3-digit octal permissions of the file /home/user/myfile.txt?

**Solution:** `754`

**Method:** We used the command:
```bash
stat -c %a /home/user/myfile.txt
```

### Question 6: What is the user id of 'admin'?

**Solution:** `1338`

**Method:** We used the command:
```bash
id -u admin
```

### Question 7: There is a user 'john' on the system. Can they write to /home/user/myfile.txt?

**Solution:** `no`

**Method:** We checked the file permissions and group membership:
```bash
ls -l /home/user/myfile.txt
groups john
```
John is in the 'admin' group, which only has read and execute permissions.

### Question 8: Can the 'admin' user execute /home/user/myfile.txt?

**Solution:** `yes`

**Method:** From the file permissions (-rwxr-xr--), we can see that the group (admin) has execute permissions.

### Question 9: Which user on the system, except for you, root, admin and john, can execute /home/user/myfile.txt?

**Solution:** `rose`

**Method:** We checked group memberships and found that Rose is in the admin group, which has execute permissions:
```bash
cat /etc/group | grep admin
```

### Question 10: /home/user/myfile.txt looks like a txt file, but it actually isn't. What kind of file is it?

**Solution:** `jpeg`

**Method:** We used the `file` command:
```bash
file /home/user/myfile.txt
```

## Flag

After answering all questions correctly using the `answer` tool, the flag should be revealed.

## Lessons Learned

This challenge tested knowledge of various Linux commands and concepts, including:
- File permissions and ownership
- User and group management
- File system navigation and information retrieval
- Basic Linux utilities like `stat`, `du`, `file`, etc.

It emphasizes the importance of being able to quickly find and interpret system and file information in a Linux environment.
