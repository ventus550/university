const express = require("express")
const app = express()

app.use(express.urlencoded({ extended: true }))
app.set("view engine", "ejs")

app.get("/", (req, res) => {
	res.render("index")
})

app.post("/print", (req, res) => {

	const data = {
		name: req.body.name,
		surname: req.body.surname,
		class: req.body.class
	}

	for (let i = 0; i < 10; i++) {
		const task = "task" + i 
		data[task] = req.body[task] || 0
	}

	if(req.body.name && req.body.surname && req.body.class) {
		res.render("print", data)
	} else {
		res.redirect("/")
	}
})

app.listen(3000)