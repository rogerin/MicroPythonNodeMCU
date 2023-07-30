const express = require('express');
const admin = require('firebase-admin');
const bodyParser = require('body-parser');

// Inicialização do Firebase
const serviceAccount = require('./firebase.json');
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
});
const db = admin.firestore();

// Inicialização do Express
const app = express();
app.use(bodyParser.json());

// Rota para receber o POST com parâmetros e salvar no banco de dados do Firebase
app.post('/iot', (req, res) => {
  const data = req.body;

  // Salva os dados no banco de dados do Firebase
  db.collection('iot_data')
    .add(data)
    .then(() => {
      res.json({ message: 'Dados salvos com sucesso no Firebase' });
    })
    .catch((error) => {
      res.status(500).json({ error: 'Ocorreu um erro ao salvar os dados no Firebase' });
    });
});



app.get('/iot2', (req, res) => {
  const data = { "luz": req.query.luz };
  console.log(data);
  // Salva os dados no banco de dados do Firebase
  db.collection('iot_data')
    .add(data)
    .then(() => {
      res.json({ message: 'Dados salvos com sucesso no Firebase' });
    })
    .catch((error) => {
      res.status(500).json({ error: 'Ocorreu um erro ao salvar os dados no Firebase' });
    });
});


app.get('/iot', (req, res) => {
    db.collection('iot_data')
      .get()
      .then((snapshot) => {
        const data = [];
        snapshot.forEach((doc) => {
          data.push(doc.data());
        });
        res.json(data);
      })
      .catch((error) => {
        res.status(500).json({ error: 'Ocorreu um erro ao obter os dados do Firebase' });
      });
  });

  
// Inicia o servidor na porta 3000
app.listen(3000, () => {
  console.log('Servidor rodando em http://localhost:3000');
});