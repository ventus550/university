const http = require('http');
const express = require("express")
const cookieParser = require('cookie-parser')


const app = express()
app.set('view engine', 'ejs');
app.set('views', './views');
app.disable('etag');
app.use(cookieParser('xzufybuixyfbuxziyfbuzixfuyb'));
app.use(express.urlencoded({ extended: true }));

const session = require('express-session');
const FileStore = require('session-file-store')(session);

const fileStoreOptions = {};


app.use(session({
	store: new FileStore(fileStoreOptions),
	secret: 'keyboard cat',
	resave: true, saveUninitialized: true
}));

// Przykład użycia ciasteczka
app.use("/", (req, res, next) => {
	var cookieValue;
	if (!req.signedCookies.cookie) {
		cookieValue = new Date().toString();
		res.cookie('cookie', cookieValue, { signed: true });
	} else {
		cookieValue = req.signedCookies.cookie;
	}
	res.setHeader('Content-Type', 'text/html');
	res.write('<p>Cookie: ' + cookieValue + '</p>');
	next()
});

// Przykład użycia session-file-store do przechowania danych sesji
app.use('/', function (req, res) {
	if (req.session.views) {
		req.session.views++;
		res.write('<p>views: ' + req.session.views + '</p>');
		res.end();
	} else {
		req.session.views = 1;
		res.end('Welcome to the file session demo. Refresh page!');
	}
});


http.createServer(app).listen(3000);