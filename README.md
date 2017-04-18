# dynamic_chart_demo
a dynamic chart demo includes a web server and a websocket server based on webix


Install node.js (ubuntu)

    curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
    sudo apt-get install -y nodejs
    
start servers

    sh start_servers.sh
    
stop servers

    sh stop_servers.sh
    
To run the testing python program "test.py", you need 

    pip install requests

To modify ui, editing the **view.html** in the path 'web_server/views'

Please refer https://docs.webix.com/desktop__components.html for the detail of the webix library.

## default demo charts
The default sample view consisted of four dynamic spline charts.

Please use http post to send a json data to the websocket server 127.0.0.1:8000/pub , channel "/data"

An example json:

    {"channel":"/data","chart1_time":"2017-04-18<br>15:19:21","chart1_d1":99,"chart1_d2":14,"chart2_time":"2017-04-18<br>15:19:21","chart2_d1":58,"chart2_d2":66,"chart3_time":"2017-04-18<br>15:19:21","chart3_d1":63,"chart3_d2":66,"chart4_time":"2017-04-18<br>15:19:21","chart4_d1":19,"chart4_d2":22}

You can use curl to send the data.
ex.

    curl -X POST -H "Contentype:application/json" -d '{"channel":"/data","chart1_time":"2017-04-18<br>15:19:21","chart1_d1":99,"chart1_d2":14,"chart2_time":"2017-04-18<br>15:19:21","chart2_d1":58,"chart2_d2":66,"chart3_time":"2017-04-18<br>15:19:21","chart3_d1":63,"chart3_d2":66,"chart4_time":"2017-04-18<br>15:19:21","chart4_d1":19,"chart4_d2":22}' localhost:8000/pub
    
or use the python testing program "test.py" to send random data

    python test.py
