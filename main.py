import numpy as np
import matplotlib.pyplot as plt
import heapq


class InteractivePathPlanner:
    def __init__(self, width=10, height=10):

        # Cria uma grid vazia
        self.grid = np.zeros((height, width), dtype=int)
        self.start = None
        self.goal = None

    def heuristic(self, a, b):
        """
        Calcula a distância de Manhattan entre dois pontos
        a e b são tuplas de coordenadas (x, y)
        """
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbors(self, node):
        # Movimentos possíveis (4 direções)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        neighbors = []
        for dx, dy in directions:
            new_x, new_y = node[0] + dx, node[1] + dy
            # Verifica se o novo nó está dentro da grid e não é um obstáculo
            if (
                0 <= new_x < self.grid.shape[1]
                and 0 <= new_y < self.grid.shape[0]
                and self.grid[new_y, new_x] != 1
            ):  # Ignora obstáculos
                neighbors.append((new_x, new_y))
        return neighbors

    def set_obstacle(self, x, y):
        """Adiciona um obstáculo na posição específica"""
        self.grid[y, x] = 1
        return self

    def set_start(self, x, y):
        """Define o ponto de início"""
        # Limpa start anterior se existir
        if self.start:
            self.grid[self.start[1], self.start[0]] = 0
        self.start = (x, y)
        self.grid[y, x] = 2
        return self

    def set_goal(self, x, y):
        """Define o ponto de objetivo"""
        # Limpa goal anterior se existir
        if self.goal:
            self.grid[self.goal[1], self.goal[0]] = 0
        self.goal = (x, y)
        self.grid[y, x] = 3
        return self

    def find_path(self):
        if not self.start or not self.goal:
            print("Defina start e goal primeiro!")
            return None

        open_set = []
        heapq.heappush(open_set, (0, self.start))
        came_from = {}
        g_score = {self.start: 0}
        f_score = {self.start: self.heuristic(self.start, self.goal)}

        while open_set:
            current = heapq.heappop(open_set)[1]

            if current == self.goal:
                # Reconstrói o caminho
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(self.start)
                return path[::-1]

            for neighbor in self.get_neighbors(current):
                tentative_g_score = g_score[current] + 1

                if (neighbor not in g_score or
                        tentative_g_score < g_score[neighbor]):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + self.heuristic(
                        neighbor, self.goal
                    )
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return None

    def visualize(self):
        """Exibe o estado atual da grid"""
        plt.figure(figsize=(10, 8))

        # Cria mapa de cores
        # 0: branco (espaço livre)
        # 1: preto (obstáculo)
        # 2: verde (início)
        # 3: vermelho (objetivo)
        cmap = plt.cm.colors.ListedColormap(["white", "black", "green", "red"])

        plt.imshow(self.grid, cmap=cmap)
        plt.title("Grid de Navegação")

        # Adiciona grade
        plt.grid(which="both", color="lightgray", linestyle="-", linewidth=0.5)
        plt.xticks(np.arange(-0.5, self.grid.shape[1], 1), [])
        plt.yticks(np.arange(-0.5, self.grid.shape[0], 1), [])

        plt.show()
        return self

    def visualize_path(self, path=None):
        plt.figure(figsize=(10, 8))

        # Mapa de cores original
        cmap = plt.cm.colors.ListedColormap(["white", "black", "green", "red", "blue"])

        # Cria uma cópia do grid para não modificar o original
        display_grid = self.grid.copy()

        # Se um caminho foi encontrado, marca-o
        if path:
            for x, y in path:
                # Marca o caminho em azul, exceto start e goal
                if (x, y) != self.start and (x, y) != self.goal:
                    display_grid[y, x] = 4

        plt.imshow(display_grid, cmap=cmap)
        plt.title("Caminho Encontrado")

        # Adiciona grade
        plt.grid(which="both", color="lightgray", linestyle="-", linewidth=0.5)
        plt.xticks(np.arange(-0.5, self.grid.shape[1], 1), [])
        plt.yticks(np.arange(-0.5, self.grid.shape[0], 1), [])

        plt.show()
        return self


planner = InteractivePathPlanner(width=15, height=15)

# Adicionando obstáculos
(
    planner.set_obstacle(5, 3)
    .set_obstacle(5, 4)
    .set_obstacle(5, 5)
    .set_obstacle(6, 5)
    .set_obstacle(7, 5)
)

# Definindo início e objetivo
(planner.set_start(2, 2).set_goal(12, 7))

# Visualizando
planner.visualize()

path = planner.find_path()
planner.visualize_path(path)
