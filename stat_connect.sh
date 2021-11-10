#/bin/bash
netstat -ant  | awk '/^tcp|^udp/{state[$6]++}END{for(i in state){print i,state[i]}}'
