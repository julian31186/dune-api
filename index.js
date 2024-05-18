const regEx = require('./utils.js').regEx;

const express = require('express'); 
  
const app = express(); 
const PORT = process.env.PORT || 3000; 

const fs = require('fs');
const json = fs.readFileSync('./scraper/data.json');

const data = JSON.parse(json);

const arr = Object.values(data);

app.listen(PORT, '0.0.0.0', () => {
    console.log(`Server is running on port ${PORT}.`);
});


app.get('/dune/random', (req, res) => {
    let randIdx = Math.floor(Math.random() * arr.length);
    res.status(200);
    let term = arr[randIdx];
    term["description"] = regEx(term["description"]);
    res.send(term);
})


app.get('/dune/:query', (req, res) => {

    let query = req.params.query;
    query = query.toLowerCase();
    
    if (query in data) {
        data[query]["description"] = regEx(data[query]["description"]);
        res.status(200);
        res.send(data[query]); 
    } else {
        res.status(400);
        res.send("Term not found");
    }
});