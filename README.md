
# GCB Tech - Post Factory

[![Instagram - GCB Tech](https://img.shields.io/badge/instagram-gcb.tech-red)](https://www.instagram.com/gcb.tech/) 

Projeto construído com o intuito de criar imagens com conteúdo para posts nas redes sociais do setor Tech do Grupo GCB, contribuindo com o programa de gameficação da área, onde buscamos disseminar os conteúdos/conhecimentos que adquirimos no dia-a-dia.


- # Recursos
    - ## Templates
        Os templates são o esqueleto do que será o seu post. Gerando um template, você receberá o ```id``` do **post**, que será usado posteriormente para gerar as imagens. Dentro da pasta gerada, você encontrará um arquivo **json**, contendo os campos que preencherão o **post**. Edite o arquivo de acordo com a necessidade e utilize o ```id``` criado para gerar o post.

        ### post simples
        Os posts simples contém apenas:
        - título
        - descrição/conteúdo do post
        - [OPCIONAL] arquivo de código (caminho)

        ```py -m cli template --type single --title MyFirstPost```

        ### _carousel_
        Os posts no formato _carousel_ contém uma lista no atríbuto _content_, do arquivo **json** do template.
        O título será utilizado na capa do _post_, e cada item da lista pode possuir seu próprio título, descrição e bloco de código.

        ```py -m cli template --type carousel --title MyFirstPost```

    - ## Post
        Após gerar o seu template, use o ```id``` gerado para gerar os arquivos de saída.
        
        ```py -m cli post --id {your_id}```

        Ao finalizar, você verá na mesma pasta gerada pelo template, o resultado na pasta _output_.


## Autores

- [@thunderjr](https://www.github.com/thunderjr)


## Licença

[MIT](https://choosealicense.com/licenses/mit/)

