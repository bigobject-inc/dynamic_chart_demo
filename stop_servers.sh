#!/bin/bash
kill $( ps ax|grep node\ web_server/web_server.js| sed -e 's/^[[:space:]]*//'| cut -d ' ' -f 1 -s)
kill $( ps ax|grep node\ websocket_server/websocket_server.js| sed -e 's/^[[:space:]]*//'| cut -d ' ' -f 1 -s)
