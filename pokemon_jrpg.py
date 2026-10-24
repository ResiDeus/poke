import random
import time

class Character:
    def __init__(self, name, hp, moves):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.moves = moves

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)

class PokemonBattle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def print_status(self):
        print("\n" + "="*30)
        print(f"{self.enemy.name:15} HP: {self.enemy.hp}/{self.enemy.max_hp}")
        print(f"{self.player.name:15} HP: {self.player.hp}/{self.player.max_hp}")
        print("="*30 + "\n")

    def execute_move(self, attacker, defender, move_name):
        print(f"¡{attacker.name} usó {move_name.upper()}!")
        time.sleep(1)

        # Base de daño aleatoria según el estilo Pokémon
        damage = random.randint(10, 25)
        
        # Efectos especiales cosméticos basados en el ataque
        if move_name in ["comer", "ternura", "bailar"]:
            damage = random.randint(5, 12)
            print(f"¡Es un movimiento táctico!")
        elif move_name in ["aruñar", "morder"]:
            if random.random() < 0.2:  # 20% de probabilidad de golpe crítico
                damage = int(damage * 1.5)
                print("¡Un golpe crítico!")

        defender.take_damage(damage)
        print(f"¡{defender.name} recibió {damage} puntos de daño!")
        time.sleep(1)

    def player_turn(self):
        print(f"¿Qué debería hacer {self.player.name}?")
        for i, move in enumerate(self.player.moves, 1):
            print(f"{i}. {move.capitalize()}")
        
        while True:
            try:
                choice = int(input("\nSelecciona un ataque (1-4): ")) - 1
                if 0 <= choice < len(self.player.moves):
                    move_selected = self.player.moves[choice]
                    self.execute_move(self.player, self.enemy, move_selected)
                    break
                else:
                    print("Opción inválida. Elige un número del 1 al 4.")
            except ValueError:
                print("Por favor, introduce un número válido.")

    def enemy_turn(self):
        print(f"¡Turno de {self.enemy.name} enemigo!")
        time.sleep(1)
        move_selected = random.choice(self.enemy.moves)
        self.execute_move(self.enemy, self.player, move_selected)

    def start(self):
        print("="*40)
        print(f"¡Un {self.enemy.name} salvaje apareció!")
        print(f"¡Adelante, {self.player.name}!")
        print("="*40)
        time.sleep(1.5)

        turn = 1
        while self.player.is_alive() and self.enemy.is_alive():
            self.print_status()
            print(f"--- TURNO {turn} ---")
            
            # Turno del Jugador
            self.player_turn()
            if not self.enemy.is_alive():
                print(f"\n¡El {self.enemy.name} enemigo se debilitó!")
                print(f"¡{self.player.name} gana la batalla!")
                break

            self.print_status()
            
            # Turno de la IA
            self.enemy_turn()
            if not self.player.is_alive():
                print(f"\n¡{self.player.name} se debilitó!")
                print("¡Has perdido la batalla! ¡A correr al Centro Pokémon!")
                break
                
            turn += 1
        print("\nFin de la simulación de batalla.")

# Configuración inicial del juego
if __name__ == "__main__":
    # Jugador 1: Perro con sus ataques solicitados
    player_dog = Character(
        name="Perro", 
        hp=100, 
        moves=["ladrar", "aruñar", "brincar", "comer"]
    )

    # IA Enemigo: Gato con sus ataques solicitados
    enemy_cat = Character(
        name="Gato", 
        hp=100, 
        moves=["meow", "ternura", "bailar", "morder"]
    )

    # Iniciar la lógica del combate
    battle = PokemonBattle(player_dog, enemy_cat)
    battle.start()
