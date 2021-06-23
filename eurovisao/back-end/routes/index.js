var express = require('express');
var router = express.Router();
var Edicao = require('../controllers/edicao')
/* GET home page. */
router.get('/edicoes', function(req, res, next) {
  Edicao.getLista()
    .then(dados => res.jsonp(dados))
    .catch(e => res.status(500).send(`Erro na listagem das edições: ${e}`))
});


router.get('/edicao/:id', function(req, res, next) {
  Edicao.getEdicao(req.params.id)
    .then(dados => res.jsonp(dados))
    .catch(e => res.status(500).send(`Erro na listagem das edições: ${e}`))
});

router.get('/musicas', function(req, res, next) {
  Edicao.getMusicas()
    .then(dados => res.jsonp(dados))
    .catch(e => res.status(500).send(`Erro na listagem das musicas : ${e}`))
});

module.exports = router;

router.get('/musicas_L_C', function(req, res, next) {
  Edicao.getMusicas_L_C()
    .then(dados => res.jsonp(dados))
    .catch(e => res.status(500).send(`Erro na listagem das musicas liricistas e compositores: ${e}`))
});

module.exports = router;
