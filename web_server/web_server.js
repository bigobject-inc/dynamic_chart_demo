var express = require("express");
var app     = express();
var path    = require("path");
var bodyParser = require('body-parser')
var fs = require('fs');

app.use(bodyParser.text());
app.use(bodyParser.urlencoded({ extended: true }));

app.use(express.static(__dirname + '/resources'));

var engine = require('consolidate');

app.set('views', __dirname + '/views');
app.engine('html', engine.mustache);
app.set('view engine', 'html');

app.listen(8888);

app.get('/',function(req,res){
//	res.sendFile(path.join(__dirname+'/template.html'));
//	res.sendFile(path.join(__dirname+'/view.html'));
	res.render("view",{jsdata:'static data from server'});
});

console.log("web server running at Port 8888");
