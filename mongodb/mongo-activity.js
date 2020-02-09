use test_db

db.createCollection('Atividades')

db.Atividades.validate()

show collections

documento = ({

“NomeSite”: “db4beginners.com”,

“categoria”: “CriarArtigo”,

“DataPrevista”: “09-23-2017”,

“keyWords”: [

“mongoDB”,

“DB4B”,

“Banco de Dados”,

“NoSQL”

],

“Finalizado”:false

})

documentoX = ({

“Site”: “db4beginners.com”,

“Categoria”: “CriarArtigo”,

“DataPublicação”: “09-23-2017”,

“PalavrasChave”: [

“mongoDB”,

“DB4B”,

“Banco de Dados”,

“NoSQL”

]})

Criar variável chamada documento1

documento1= ({

“NomeSite”: “db4beginners.com”,

“titulo”: “Instalação MongoDB”,

“categoria”: “ValidarArtigo”,

“DataPrevista”: “09-24-2017”,

“DataPublicaçao”: “09-25-2017”,

“keyWords”: [

“mongoDB”,

“DB4B”,

“Banco de Dados”,

“NoSQL”

],

“Finalizado”:true

});

Criar variável chamada documento2

documento2= ({

“_id” : “Dani”,

“NomeSite”: “DB4B.co“,

“titulo”: “Certificação SQL Server”,

“categoria”: “Gravar Vídeo”,

“Canal Youtube”: “DB4Beginners”,

“keyWords”: [

“SQL Server 2016”,

“70-761”,

“Banco de Dados”,

“Relacional”

],

“Finalizado”:true

})

// ================================

db.Atividades.insert(documento)

db.Atividades.insertMany([ documento, documento ])

db.Atividades.count()

// ================================

db.Atividades.find()


db.Atividades.find().pretty()


db.Atividades.findOne()

db.Atividades.find(
    {},
    { _id: 0 }
)

db.Atividades.find().sort({ categoria: -1 }).pretty()

db.Atividades.find().limit(3).pretty()

db.Atividades.distinct('categoria')

db.Atividades.find(

    { Finalizado: false },
    { _id: 0 }

)


