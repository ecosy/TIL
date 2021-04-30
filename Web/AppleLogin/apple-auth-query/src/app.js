const express = require('express');
const app = express();
const fs = require('fs');
const config = fs.readFileSync('./config/config.json');
const AppleAuth = require('apple-auth');
const bodyParser = require('body-parser');
const jwt = require('jsonwebtoken');
const { json } = require('body-parser');

let auth = new AppleAuth(config, fs.readFileSync('./config/AuthKey.p8').toString(), 'text');

// app.get('/auth', async (req, res) => {
//     console.log("i got /auth get");
//     const code = req.query.code;
//     console.log("code : " + code);
//     res.send("i got /auth get, code : "+ code);

//     try{
//         // const response = await auth.accessToken(code);
//         // const idToken = jwt.decode(response.id_token);
//         // const user = {};
//         // user.id = idToken.sub;

//         // if (idToken.email) user.email = idToken.email;
//         // if (req.body.user) {
//         //     const { name } = JSON.parse(req.body.user);
//         //     user.name = name;
//         // }
//         // res.json(user);
//         // console.log("id token : " + idToken);

//         await auth.accessToken(code).then(function(data){
//             console.log("data : " + data);

//             var jsonData = data.json;
//             for (var key in jsonData){
//                 console.log("key : " + key + " value : " + jsonData[key])
//             }
//         }).catch(function(err){
//             console.error(err);
//         });

//     }catch(ex){
//         console.error(ex);
//         res.send("Error, GET, /auth");
//     }
//     console.log("func end...")
// });

app.get('/auth', async (req, res) => {
    console.log("i got /auth get");
    const code = req.query.code;
    console.log("code : " + code);
    res.send("i got /auth get, code : "+ code);

    try{
        const response = await auth.accessToken(code); 
        const idToken = jwt.decode(response.id_token); 
        const email = idToken.email; 
        const sub = idToken.sub;

        console.log("id token : " + idToken)
        console.log("email : " + email)
        console.log("sub : " + sub)

    }catch(ex){
        console.error(ex);
        res.send("Error, GET, /auth");
    }
    console.log("func end...")
});

app.get("/", (req, res) => {
    console.log( Date().toString() + "GET /");
    const loginURL = "https://appleid.apple.com/auth/authorize?client_id=com.hyundai.appleLogin&redirect_uri=https://host.docker.internal:9000/nginx&response_mode=query&response_type=code&state=itsMyState"
    res.send(`<a href="${loginURL}">Sign in with Apple</a>`);
});

app.get('/token', (req, res) => {
    res.send(auth._tokenGenerator.generate());
});

app.post('/auth', bodyParser(), async (req, res) => {
    console.log("i got /auth post");
    console.log("post code : " + req.body.code);
    
    res.send("i got /auth post, code : " + req.body.code);
});

// app.get('/auth', async (req, res) => {
//     console.log("i got /auth get");
//     const code = req.query.code;
//     console.log("code : " + code);
//     res.send("i got /auth get, code : "+ code);
// });

// app.post('/auth', bodyParser(), async (req, res) => {
//     try {
//         console.log( Date().toString() + "POST /auth");
//         const response = await auth.accessToken(req.body.code);
//         const idToken = jwt.decode(response.id_token);

//         const user = {};
//         user.id = idToken.sub;

//         if (idToken.email) user.email = idToken.email;
//         if (req.body.user) {
//             const { name } = JSON.parse(req.body.user);
//             user.name = name;
//         }

//         res.json(user);
//     } catch (ex) {
//         console.error(ex);
//         res.send("An error occurred!");
//     }
// });

// app.get('/auth', (req, res) => {
//     console.log( Date().toString() + "GET /auth");
//     const code = req.query.code;

//     try{
//         console.log("i got a code!! code : " + code)
//     }catch(ex){
//         console.error(ex);
//         res.send("Error, GET, /auth");
//     }
//     res.send("get /auth");
// });

app.get('/refresh', async (req, res) => {
    try {
        console.log( Date().toString() + "GET /refresh");
        const accessToken = await auth.refreshToken(req.query.refreshToken);
        res.json(accessToken);
    } catch (ex) {
        console.error(ex);
        res.send("Error, GET, /refresh");
    }
});

app.listen(8888, () => {
    console.log("Listening on http://localhost");
});
