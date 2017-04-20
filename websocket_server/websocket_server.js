
var bodyParser = require('body-parser')
var express = require('express'),
    faye = require('faye'),http = require('http');

var app = express(),
    server = http.createServer(app),
    bayeux = new faye.NodeAdapter({mount: '/faye'});

bayeux.on('publish', function(clientId, channel, data) {
	console.log(channel + " " + JSON.stringify(data));
})

app.use(bodyParser.json());
app.use(bodyParser.text());
app.use(express.static(__dirname + '/public'));

// "/pub" to receive data
app.post('/pub', function(req, res) {
	var ts = Date.now();
	var tmp_v = req.body;
	tmp_v.id=ts;
	//make a json document for the faye message server
	var test_json= {"id":ts,"data":tmp_v,"operation":"insert","Hr":true,"clientId":9999};

	// publish the message to the assigned channel
	bayeux.getClient().publish(tmp_v.channel, test_json );

	res.sendStatus(200);
});

bayeux.attach(app.listen(8000, function() {}));
console.log("websocket server running at Port 8000");
