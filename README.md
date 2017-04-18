# dynamic_chart_demo
a dynamic chart demo includes a web server and a websocket server based on webix


Install node.js (ubuntu)

    curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
    sudo apt-get install -y nodejs
    
start servers

    sh start_servers.sh
    
stop servers

    sh stop_servers.sh
    
To run the testing python program, you need 

    pip install requests

To modify ui, editing the view.html in the path 'web_server/views'
