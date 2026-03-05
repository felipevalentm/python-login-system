import getpass

usuarios = {
"felipe": "felipe123",
"admin": "admin123",
"joao": "joao123",
"maria": "maria123",
"carlos": "carlos123",
"ana": "ana123",
"lucas": "lucas123",
"juliana": "juliana123",
"roberto": "roberto123",
"fernanda": "fernanda123",
"bruno": "bruno123",
"camila": "camila123",
"ricardo": "ricardo123",
"patricia": "patricia123",
"marcos": "marcos123",
"aline": "aline123",
"gabriel": "gabriel123",
"rafael": "rafael123",
"leticia": "leticia123",
"diego": "diego123",
"thiago": "thiago123",
"paulo": "paulo123",
"renata": "renata123",
"andre": "andre123",
"eduardo": "eduardo123",
"beatriz": "beatriz123",
"leonardo": "leonardo123",
"gustavo": "gustavo123",
"daniela": "daniela123",
"vinicius": "vinicius123",
"larissa": "larissa123",
"pedro": "pedro123",
"sabrina": "sabrina123",
"matheus": "matheus123",
"luana": "luana123",
"fabio": "fabio123",
"tatiane": "tatiane123",
"henrique": "henrique123",
"rodrigo": "rodrigo123",
"mariana": "mariana123",
"danilo": "danilo123",
"karina": "karina123",
"samuel": "samuel123",
"vitoria": "vitoria123",
"alex": "alex123",
"isabela": "isabela123",
"sergio": "sergio123",
"aline.s": "aline123",
"leo.silva": "leo123",
"usuario_teste": "teste123"
}

def login_validador(): 
    
    tentativas = 3

    while tentativas > 0:
        usuario = input("Usuário: ")
        senha = getpass.getpass("Senha: ")

        if usuario in usuarios and usuarios[usuario] == senha:
            print("Login realizado com sucesso!")
            break
        else:
            tentativas -= 1 
            print(f"Credenciais inválidas. Tentativas restantes: {tentativas}")

    if tentativas == 0:
     print("Conta bloqueada")

login_validador()
