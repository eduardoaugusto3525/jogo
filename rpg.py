import random

class Personagem:
    def __init__(self, nome, forca, defesa, vida):
        self.nome = nome
        self.forca = forca
        self.defesa = defesa
        self.vida = vida
    
    def atacar(self, alvo):
        dano_bruto = self.forca + random.randint(-3, 3)
        dano_final = max(0, dano_bruto - alvo.defesa)
        alvo.vida -= dano_final
        print(f"{self.nome} ataca {alvo.nome} e causa {dano_final} de dano!")

    def defender(self):
        defesa_bonus = random.randint(1, 5)
        self.defesa += defesa_bonus
        print(f"{self.nome} se defende e aumenta a defesa em {defesa_bonus} pontos temporariamente.")
        return defesa_bonus

    def restaurar_defesa(self, defesa_bonus):
        self.defesa -= defesa_bonus

    def esta_vivo(self):
        return self.vida > 0

# Criação dos personagens
jogador = Personagem("Herói", forca=10, defesa=5, vida=50)
inimigo = Personagem("Vilão", forca=8, defesa=3, vida=40)

# Função para o turno do jogador
def turno_jogador():
    print("\nEscolha sua ação:")
    print("1 - Atacar")
    print("2 - Defender")
    escolha = input("Escolha: ")

    if escolha == "1":
        jogador.atacar(inimigo)
    elif escolha == "2":
        defesa_bonus = jogador.defender()
        return defesa_bonus
    else:
        print("Escolha inválida! Perdeu a vez.")
    return 0

# Função para o turno do inimigo
def turno_inimigo():
    if inimigo.vida < 15 and random.choice([True, False]):
        defesa_bonus = inimigo.defender()
        return defesa_bonus
    else:
        inimigo.atacar(jogador)
    return 0

# Loop de batalha
while jogador.esta_vivo() and inimigo.esta_vivo():
    print("\nStatus dos Personagens:")
    print(f"{jogador.nome} - Vida: {jogador.vida}, Defesa: {jogador.defesa}")
    print(f"{inimigo.nome} - Vida: {inimigo.vida}, Defesa: {inimigo.defesa}")
    
    # Turno do jogador
    defesa_bonus_jogador = turno_jogador()
    
    # Verifica se o inimigo ainda está vivo
    if inimigo.esta_vivo():
        # Turno do inimigo
        defesa_bonus_inimigo = turno_inimigo()
        
        # Restaurar defesa temporária
        if defesa_bonus_inimigo > 0:
            inimigo.restaurar_defesa(defesa_bonus_inimigo)
    
    # Restaurar defesa temporária do jogador
    if defesa_bonus_jogador > 0:
        jogador.restaurar_defesa(defesa_bonus_jogador)

# Fim do jogo
if jogador.esta_vivo():
    print(f"\nParabéns! {jogador.nome} venceu a batalha!")
else:
    print(f"\n{inimigo.nome} venceu a batalha. Tente novamente!")
