const express = require('express');
const https = require('https');
const app = express();
const port = process.env.PORT || 5000;
var cors = require("cors");
var bodyParser = require('body-parser')

app.use(cors());
app.use(bodyParser.json())

// console.log that your server is up and running
app.listen(port, () => console.log(`Listening on port ${port}`));

// create a GET route






app.post('/express_backend', (req, respond) => {
// console.log(req.body.content);
// console.log(req.body.page);
var searchUrl = 'https://hn.algolia.com/api/v1/search?query='+ req.body.content+'&page='+req.body.page+'&hitsPerPage=20';
var newsUrl = 'https://hn.algolia.com/api/v1/search_by_date?tags=story&page='+req.body.page+'&hitsPerPage=20';
var Url = null;
// console.log(req.body.type);
if (req.body.type == 'search'){
    Url = searchUrl;
}else{
    // console.log('im in');
    Url = newsUrl;
}

https.get(Url, function (res) {
    var json = '';
    res.on('data', function (chunk) {
        json += chunk;
    });

    res.on('end', function () {
        if (res.statusCode === 200) {
            try {
                var data = JSON.parse(json);
                // data is available here:
                const { hits, page } = data;
                // console.log(hits[0]);
                // console.log(page);
                // console.log(hits.length);
                respond.send(hits);

                // console.log(page);
            } catch (e) {
                console.log('Error parsing JSON!');
                
            }
        } else {
            console.log('Status:', res.statusCode);
        }
    });
}).on('error', function (err) {
    console.log('Error:', err);
});
// console.log('111')

});