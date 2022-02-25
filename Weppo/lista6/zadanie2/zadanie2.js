const express = require("express")
const app = express()

app.use(express.urlencoded({ extended: true }))
app.set("view engine", "ejs")

app.get('/', (req, res) => {
    const checkboxes = {
        boxes: [
            { name: "box", text: "First"},
            { name: "pox", text: "Second"},
            { name: "fox", text: "Third"}
        ]
    }

    res.render('index', checkboxes)
})

app.listen(3000)