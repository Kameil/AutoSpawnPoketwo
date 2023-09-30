# AutoSpawnPoketwo
### Links

- [replit](https://replit.com/@Raquison/AutoSpawnPoketwo)
- [github](https://github.com/Kameil/AutoSpawnPoketwo/tree/main)

## Como usar?

#### Token
![Secret/token](https://media.discordapp.net/attachments/1128720966575464488/1157723454808801351/Screenshot_37.png?ex=6519a57d&is=651853fd&hm=a5f97896b28019770d1f75fe670f5cbadf9b597b2f6f72f99126bb8b3a0e32e3&= "Secret/token")

- Voce deve criar um [secret](https://docs.replit.com/programming-ide/workspace-features/secrets) [token](https://pt.thefilibusterblog.com/chto-takoe-token-discord-i-kak-ego-poluchit/) e colocar o [token](https://pt.thefilibusterblog.com/chto-takoe-token-discord-i-kak-ego-poluchit/) da sua conta do discord.


#### Spam id
![secret/spam_id](https://media.discordapp.net/attachments/1128720966575464488/1157724603574132766/Screenshot_38.png?ex=6519a68e&is=6518550e&hm=e567da44ca230b838800a374d078ac7fc5e9cdd3ea92ec0320e2548fe0df01ba&= "secret/spam_id")

- Voce deve Criar um [secret](https://docs.replit.com/programming-ide/workspace-features/secrets) **"spam_id"** Com o [id do canal](https://media.discordapp.net/attachments/1128720966575464488/1157726926027358258/Screenshot_40.png?ex=6519a8b8&is=65185738&hm=d1e0dda82854d779aa52e3563b1bfe73a8dc5a5bc8b050b99799968c4014d3b1&=) que o bot deve spamar.


#### Run
![run replit](https://media.discordapp.net/attachments/1128720966575464488/1157725964726444133/Screenshot_39.png?ex=6519a7d3&is=65185653&hm=107dab85b8f4333ed08e779b02e69df08ef0bdc3a7df5b8616f7ac5e5a162673&= "run replit")

- **"ctrl + enter ou clique no botao run"**
Comando de run: **python3 main.py**


## Erros comuns
#### discord.LoginFailure

![improper token](https://media.discordapp.net/attachments/1128720966575464488/1157403387571216384/Screenshot_32.png?ex=65187b67&is=651729e7&hm=bdebd0250553c806c2dcadc566b6d43feb8546c6edd143e33a00aa42b64ea44a&= "improper token")

- Esse erro acontece quando o token que voce colocou no secret **token** esta invalido.


#### Intents

![missing intents](https://media.discordapp.net/attachments/1128720966575464488/1157462172851507271/Screenshot_35.png?ex=6518b226&is=651760a6&hm=ba6d37febb6a8754c246bd8bb030f16ddaa509d462e0ba6264ff4e25a96acc69&= "missing intents")

- Esse erro acontece quando a biblioteca discord.py se sobrepoe a discord.py-self para resolver e so executar o comando: **pip uninstall discord.py-self && pip install discord.py-self==2.0.0**


