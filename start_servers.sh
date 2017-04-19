#!/bin/bash

node websocket_server/websocket_server.js &
sleep 1
node web_server/web_server.js 

