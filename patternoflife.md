# Pattern of Life
Hackers have breached our network. We know they are there, hiding in the shadows as users continue to browse the web like normal. As a threat hunter, your job is to constantly be searching our environment for any signs of malicious behavior.

Today you just received a packet capture (pcap) from a user's workstation. We think that an attacker may have compromised the user's machine and that the computer is beaconing out to their command and control (C2) server. Based on some other logs, we also think the attacker was *not* using a fully encrypted protocol and also did not put much care into making their C2 server look like a normal website. Your task? We'd like you to submit the port number that the C2 server is listening on in the form of MetaCTF{portnumber} as the flag.

## Solve
So from the prompt, we know we should look at HTTP(S) things. HTTP Command and Control beaconing is a thing.

1. Look at the HTTP Objects: File -> Export Objects -> HTTP Objects
2. Notice the port is 8080

`MetaCTF{8080}`