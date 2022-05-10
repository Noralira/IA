from games.tintas.players.greedy import GreedyTintasPlayer
from games.tintas.players.human import HumanTintasPlayer
from games.tintas.players.minimax import MinimaxTintasPlayer
from games.tintas.players.random import RandomTintasPlayer
from games.tintas.simulator import TintasSimulator
from games.game_simulator import GameSimulator


def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()

def read_player():
    while True:
        menuSelect = int(input("\nPlease select one of the four options: "))
        if menuSelect == 1:
            return HumanTintasPlayer("Human")
            
        elif menuSelect == 2:
            return MinimaxTintasPlayer("Minimax")
            
        elif menuSelect == 3:
            return GreedyTintasPlayer("Greedy")
        
        elif menuSelect == 4:
            return RandomTintasPlayer("Random")
            
        else:
            print("The selection provided is invalid.")    

def main():
    player1= None
    player2= None

    print("ESTG IA Games Simulator")
    print("\n\t\tMain Menu - Escolhe o jogador 1")
    print("\t1. Human")
    print("\t2. minimax")
    print("\t3. greedy")
    print("\t4. random")
    player1 = read_player()
    

    print("\n\t\tMain Menu - Escolhe o jogador 2")
    print("\t1. Human")
    print("\t2. minimax")
    print("\t3. greedy")
    print("\t4. random")
    
    player2 = read_player()
    
    num_iterations = 4

  
    run_simulation("simulacao", TintasSimulator(player1, player2), num_iterations)

if __name__ == "__main__":
    main()
