// This loads the settings from your `.env` file.
require("dotenv").config();
const express = require("express");
const db = require("./db/database");

const app = express();

const PORT = 3333;

////////////
// Routes //
////////////

// The home page lists some available URLs.
app.get("/", (req, res) => {
    res.json({
        urls: {
            get_all: `localhost:${PORT}/api`,
            get_1: `localhost:${PORT}/api/1`,
            get_a_different_one: `localhost:${PORT}/api/2`,
            search: `localhost:${PORT}/search/beh`,
            search: `localhost:${PORT}/search/r`,
        },
    });
});

// list all customers
app.get("/api", (req, res) => {
    db.getAllCustomers()
        .then(data => res.json(data))
        .catch(err => res.status(500).json(err));
});

// get a monster by ID (1, 2, or 3)
app.get("/api/:id", (req, res) => {
    const id = req.params.id;

    db.getCustomersById(id)
        .then(data => {
            if (data.length > 0) {
                console.log("data", data);
                res.json(data);
            } else {
                res.status(404).json({ message: "Not Found" });
            }
        })
        .catch(err => res.status(500).json(err));
});

// Search the database by monster name
app.get("/api/search/:keyword", (req, res) => {
    const keyword = req.params.keyword;
    db.searchCustomersByName(keyword)
        .then(data => res.json(data))
        .catch(err => res.status(500).json(err));
});

app.listen(PORT, () => console.log(`listening at http://localhost:${PORT}`));