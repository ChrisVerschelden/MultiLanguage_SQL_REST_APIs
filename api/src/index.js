const express = require("express");
const sql = require('mysql')
const app = express();
const PORT = 3333;
const conn = sql.createConnection({
    host: 'mariadb', 
    user:'maria', 
    password: 'maria',
    database : 'mydatabase'
});

conn.connect(function(err) {
    if (err) throw err;
    console.log("You are connected!");
  });

app.get('/customers', (req, res) =>{    
    conn.query('select * from customers', (err, results) => {
        if(err) throw err
        res.end(JSON.stringify(results)); // Result in JSON format
    });
})
    

app.get("/customers/:id", (req, res) => {
    const id = req.params.id;

    conn.query('SELECT * FROM customers WHERE id ='+id, (err, results)=>{
        if(err) throw err
        res.end(JSON.stringify(results)); // Result in JSON format
    });
})

app.delete("/customers/:id", (req, res) => {
    const id = req.params.id;

    conn.query('delete FROM customers WHERE id ='+id, (err, results)=>{
        if(err) throw err
        res.end(JSON.stringify(results)); // Result in JSON format
    });
})

app.post("/customers/", (req, res) => {
    const firstname = req.query.firstname;
    const name = req.query.name;
    const email = req.query.email;


    conn.query(`Insert into customers (firstname, name, email) values ('`+firstname+`','`+name+`','`+email+`')`, (err, results)=>{
        if(err) throw err
        res.end(JSON.stringify(results)); // Result in JSON format
    });
})


app.put("/customers/:id", (req, res) => {
    const id = req.params.id;

    const firstname = req.query.firstname;
    const name = req.query.name;
    const email = req.query.email;


    conn.query(`Update customers SET firstname ='`+firstname+`', name ='`+name+`', email ='`+email+`' where id = `+id, (err, results)=>{
        if(err) throw err
        res.end(JSON.stringify(results)); // Result in JSON format
    });
})




app.listen(PORT, () => console.log(`listening at http://localhost:${PORT}`));