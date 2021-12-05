# The Searcher
Alright analyst. We need your help with some investigative work as we dive deeper into one of the infections on our company's network. We've taken a small packet capture that we know contains some C2 traffic. In order to give us some more leads for the investigation though, we'd like to see if we can identify what C2 framework the attacker was using. This will give us some leads into potential host-based artifacts that might be left behind.

Please submit the name of the C2 Framework being used in the form of MetaCTF{c2frameworkname}

## Solve 
Looking at the pcap -> notice the user agent (this is a good way to identify C2 frameworks).

```
GET /en-us/docs.html HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36
Host: 52.44.115.131:8080
Cookie: ASPSESSIONID=fc1060eace; SESSIONID=1552332971750

HTTP/1.1 200 OK
Date: Mon, 22 Nov 2021 01:33:24 GMT
Content-Type: text/plain; charset=utf-8
Server: Microsoft-IIS/7.5
Transfer-Encoding: chunked
```

Google search on the SESSIONID: find [GitHub](https://github.com/sclow/covenant_mgmt/blob/main/config.yml.example)

`MetaCTF{Covenant}`

