const express = require('express'); 
  
const app = express(); 
const PORT = 3000; 

const fs = require('fs');
const json = fs.readFileSync('../scraper/data.json');

const data = JSON.parse(json);

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}.`);
});

app.get('/dune/:query', (req, res)=>{

    let query = req.params.query;
    query = query.toLowerCase();
    
    if (query in data) {
        res.status(200);
        data[query]["description"] = data[query]["description"]
        .replace(/[\n\r\t]+/g, ' ')
        .replace(/\s+/g, ' ')
        .replace(/"/g, "'")
        .trim();
        res.send(data[query]); 
    } else {
        res.status(400);
        res.send("Term not found");
    }
});