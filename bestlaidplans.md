# The Best Laid Plain
Sometimes, routers can break packets up into fragments to meet abnormal networking requirements, and the endpoint will be responsible for putting these back together. Sometimes however, this doesn't go as planned, as Microsoft found out with CVE-2021-24074. We'd like to see the function responsible for this vulnerability, but we're having some trouble finding its name... Could you see if you could find it?

## Solve
https://duckduckgo.com/?q=%22CVE-2021-24074%22+writeup&t=ffab&ia=web

https://www.armis.com/blog/from-urgent11-to-frag44-microsoft-patches-critical-vulnerabilities-in-windows-tcpip-stack/

`MetaCTF{Ipv4pReceiveRoutingHeader}`