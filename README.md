# AutoSpawnPoketwo
### Links

- [replit](https://replit.com/@Raquison/AutoSpawnPoketwo)
- [github](https://github.com/Kameil/AutoSpawnPoketwo/tree/main)

## Como usar?

#### Token
![Secret/token](https://raw.githubusercontent.com/Kameil/arquivos-para-eu-da-uns-request-tendeu/main/imagens/Screenshot_37.png "Secret/token")

- Voce deve criar um [secret](https://docs.replit.com/programming-ide/workspace-features/secrets) [token](https://pt.thefilibusterblog.com/chto-takoe-token-discord-i-kak-ego-poluchit/) e colocar o [token](https://pt.thefilibusterblog.com/chto-takoe-token-discord-i-kak-ego-poluchit/) da sua conta do discord.


#### Spam id
![secret/spam_id](https://raw.githubusercontent.com/Kameil/arquivos-para-eu-da-uns-request-tendeu/main/imagens/Screenshot_38.png "secret/spam_id")

- Voce deve Criar um [secret](https://docs.replit.com/programming-ide/workspace-features/secrets) **"spam_id"** Com o [id do canal](https://media.discordapp.net/attachments/1128720966575464488/1157726926027358258/Screenshot_40.png?ex=6519a8b8&is=65185738&hm=d1e0dda82854d779aa52e3563b1bfe73a8dc5a5bc8b050b99799968c4014d3b1&=) que o bot deve spamar.


#### Run
![run replit](https://raw.githubusercontent.com/Kameil/arquivos-para-eu-da-uns-request-tendeu/main/imagens/Screenshot_39.png "run replit")

- **"ctrl + enter ou clique no botao run"**
Comando de run: **python3 main.py**


------------



## Erros comuns
#### discord.LoginFailure

![improper token](https://raw.githubusercontent.com/Kameil/arquivos-para-eu-da-uns-request-tendeu/main/imagens/Screenshot_32.png "improper token")

- Esse erro acontece quando o token que voce colocou no secret **token** esta invalido.


#### Intents

![missing intents](https://raw.githubusercontent.com/Kameil/arquivos-para-eu-da-uns-request-tendeu/main/imagens/Screenshot_35.png "missing intents")

- Esse erro acontece quando a biblioteca discord.py se sobrepoe a discord.py-self para resolver e so executar o comando: **pip uninstall discord.py-self && pip install discord.py-self==2.0.0**

------------


## Comandos
- command_prefix = "!"

#### Start
- Ao digitar **!start** no canal cujo o id esta no spam id o bot ira despausar ou enviar uma mensagem informando que nao esta pausado.

#### Stop
- Ao digitar **!stop** no canal cujo o id esta no spam_id o bot ira pausar ou enviar uma mensagem indicando que esta pausado.


------------

