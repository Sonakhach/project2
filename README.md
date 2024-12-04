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
![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-04_03_08_45.png)
![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-04_03_11_10.png)
![im1](https://github.com/Sonakhach/project2/blob/main/Screenshot_2024-12-04_03_14_12.png)

