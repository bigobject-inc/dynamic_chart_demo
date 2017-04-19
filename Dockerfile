FROM ubuntu:14.04
MAINTAINER Eugene Lai <eugene@bigobject.io>

RUN apt-get update && apt-get install -y curl git

RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -

RUN sudo apt-get install -y nodejs

RUN git clone https://github.com/bigobject-inc/dynamic_chart_demo.git

VOLUME /dynamic_chart_demo/web_server/views/

EXPOSE 8000 8888

WORKDIR /dynamic_chart_demo
RUN chmod +x /dynamic_chart_demo/start_servers.sh /dynamic_chart_demo/stop_servers.sh

CMD ./start_servers.sh


 








