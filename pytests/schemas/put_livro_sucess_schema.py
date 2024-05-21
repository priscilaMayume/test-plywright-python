put_livro_sucess_schema = {
"type": "object",
"properties": {
    "id": {
        "type": "integer"
    },
    "nome": {
        "type": "string"
    },
    "autor": {
        "type": "string"
    },
    "data_publicacao": {
        "type": "string"
    },
    "qtde_paginas": {
        "type": "integer"
    },
    "created_on": {
        "type": "string"
    },
    "update_at": {
        "type": "string"
    }
},
"required": [
    "id",
    "nome",
    "autor",
    "data_publicacao",
    "qtde_paginas",
    "created_on",
    "update_at"
]
}