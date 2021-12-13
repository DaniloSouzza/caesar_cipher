# Caesar's Cipher

THE CAESAR'S CIPHER

In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.



---
WKH FDHVDU*V FLSKHU

Lq fu|swrjudsk|/ d Fdhvdu flskhu/ dovr nqrzq dv Fdhvdu*v flskhu/ wkh vkliw flskhu/ Fdhvdu*v frgh ru Fdhvdu vkliw/ lv rqh ri wkh vlpsohvw dqg prvw zlgho| nqrzq hqfu|swlrq whfkqltxhv1 Lw lv d w|sh ri vxevwlwxwlrq flskhu lq zklfk hdfk ohwwhu lq wkh sodlqwh{w lv uhsodfhg e| d ohwwhu vrph il{hg qxpehu ri srvlwlrqv grzq wkh doskdehw1

Iru h{dpsoh/ zlwk d ohiw vkliw ri 6/ G zrxog eh uhsodfhg e| D/ H zrxog ehfrph E/ dqg vr rq1 Wkh phwkrg lv qdphg diwhu Mxolxv Fdhvdu/ zkr xvhg lw lq klv sulydwh fruuhvsrqghqfh1

---
A simple project to explore a little more about Jenkins and It's functionalities.
I decided to create a simple project using `Flask`, `Docker` and finally `Jenkins` to run the tests and then deploy the application.

It was a very good approach to understand a little bit more about Jenkins configurations and the JenkinsFile.

## Usage

You can simply run the `app.py` file or configure a jenkins by your own, with no necessity do download anything.
The flow will be:
- Download of repository into jenkins workspace;

- Install all requirements in the machine - It is not necessary to install everything because the application will run inside a container, you can simply install pytest, that would be necessary to run the initial tests;

- After testing and If everything is running well, we will create a docker from *.dockerfile with python, installing all the requirements and the start It on port 80;

- Finally we will run our container in detached mode, exposing the port 80, and voilá :)

Hope you enjoy.
