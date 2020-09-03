# 0x14. MySQL

## Resources:books:
Read or watch:
* [What is a primary-replica cluster](https://intranet.hbtn.io/rltoken/yI-YnEyAx2mO5qqmbrCTbw)
* [MySQL primary replica setup](https://intranet.hbtn.io/rltoken/M2mXERIEQA7w0Pkj85nTNw)
* [Build a robust database backup strategy](https://intranet.hbtn.io/rltoken/7C7YTJOU2iR_kZDQLPhl1A)

---
## Learning Objectives:bulb:
What you should learn from this project:

* What is the main role of a database
* What is a database replica
* What is the purpose of a database replica
* Why database backups need to be stored in different physical locations
* What operation should you regularly perform to make sure that your database backup strategy actually works

---
---

## Author
* **Katorea** - [Katorea132](https://github.com/Katorea132)

GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
CREATE DATABASE tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (id INT, name VARCHAR(256));
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%' IDENTIFIED BY '1152';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
INSERT INTO nexus6 VALUES(1, 'Pizza');
