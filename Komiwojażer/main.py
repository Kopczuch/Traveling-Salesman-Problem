import tkinter as tk
from PIL import ImageTk, Image
import math
import random

# WSPÓŁRZĘDNE MIAST
# <editor-fold desc="Współrzędne">
wspMiast = [[510, 162], [228, 170], [264, 58],  [284, 430],
            [378, 372], [339, 448], [486, 336], [308, 292],
            [362, 108], [222, 391], [166, 234], [458, 444],
            [41, 137],  [394, 248], [170, 351], [87, 272]]
#Białystok wspMiast[0]
xBial = 510
yBial = 162
#Bydgoszcz wspMiast[1]
xByd = 228
yByd = 170
#Gdańsk wspMiast[2]
xGd = 264
yGd = 58
#Katowice wspMiast[3]
xKat = 284
yKat = 430

#Kielce wspMiast[4]
xKiel = 378
yKiel = 372
#Kraków wspMiast[5]
xKr = 339
yKr = 448
#Lublin wspMiast[6]
xLub = 486
yLub = 336
#Łódź wspMiast[7]
xBoat = 308
yBoat = 292

#Olsztyn wspMiast[8]
xOl = 362
yOl = 108
#Opole wspMiast[9]
xOp = 222
yOp = 391
#Poznań wspMiast[10]
xPoz = 166
yPoz = 234
#Rzeszów wspMiast[11]
xRz = 458
yRz = 444

#Szczecin wspMiast[12]
xSz = 41
ySz = 137
#Warszawa wspMiast[13]
xWar = 394
yWar = 248
#Wrocław wspMiast[14]
xWro = 170
yWro = 351
#Zielona Góra wspMiast[15]
xZg = 87
yZg = 272
# </editor-fold>


# FUNCTIONS
# mapa
# funkcja do wybierania miast
def submit(miasto):
    # <editor-fold desc="Oznaczenie wybranego miasta">
    if miasto == "Wybierz miasto startowe":
        x0 = 0
        y0 = 0
    if miasto == "Białystok":
        x0 = xBial
        y0 = yBial
    if miasto == "Bydgoszcz":
        x0 = xByd
        y0 = yByd
    if miasto == "Gdańsk":
        x0 = xGd
        y0 = yGd
    if miasto == "Katowice":
        x0 = xKat
        y0 = yKat
    if miasto == "Kielce":
        x0 = xKiel
        y0 = yKiel
    if miasto == "Kraków":
        x0 = xKr
        y0 = yKr
    if miasto == "Lublin":
        x0 = xLub
        y0 = yLub
    if miasto == "Łódź":
        x0 = xBoat
        y0 = yBoat
    if miasto == "Olsztyn":
        x0 = xOl
        y0 = yOl
    if miasto == "Opole":
        x0 = xOp
        y0 = yOp
    if miasto == "Poznań":
        x0 = xPoz
        y0 = yPoz
    if miasto == "Rzeszów":
        x0 = xRz
        y0 = yRz
    if miasto == "Szczecin":
        x0 = xSz
        y0 = ySz
    if miasto == "Warszawa":
        x0 = xWar
        y0 = yWar
    if miasto == "Wrocław":
        x0 = xWro
        y0 = yWro
    if miasto == "Zielona Góra":
        x0 = xZg
        y0 = yZg
    # </editor-fold>
    canvas.delete("circle", "line")
    if x0!=0:
        canvas.create_oval(x0-5, y0-5, x0+5, y0+5, width=2, fill="red", tags="circle")


# funkcja do resetowania mapy
def reset():
    canvas.delete("line", "circle")
    wybraneMiasto.set("Wybierz miasto startowe")
    a1.set(0)
    a2.set(0)
    a3.set(0)
    a4.set(0)


# funkcja do rysowania ścieżki na mapie
def draw(path, wspMiast, color):
    if path == None:
        return
    for i in range(len(path)-1):
        node = path[i]
        next_node = path[i+1]
        canvas.create_line(wspMiast[node][0], wspMiast[node][1], wspMiast[next_node][0], wspMiast[next_node][1],
                           tags="line", fill=color)
    canvas.create_line(wspMiast[path[-1]][0], wspMiast[path[-1]][1], wspMiast[path[0]][0], wspMiast[path[0]][1],
                       tags="line", fill=color)


# ALGORYTMY
# funkcja do określania dystansu pomiędzy miastami
def distance(x0, y0, x1, y1):
    return math.sqrt((x0 - x1)**2 + (y0 - y1)**2)


# funckja do obliczania kosztu(długości) ścieżki
def cost(list, wspMiast):
    path = 0
    for i in range(len(list)-1):
        m1 = list[i]
        m2 = list[i+1]
        a = distance(wspMiast[m1][0], wspMiast[m1][1], wspMiast[m2][0], wspMiast[m2][1])
        path += a
    path += distance(wspMiast[0][0], wspMiast[0][1], wspMiast[-1][0], wspMiast[-1][1])
    return path


# funkcja zamieniająca nazwę miasta na jego numer
def city_to_number(miasto):
    node = -1
    if miasto == "Białystok":
        node = 0
    elif miasto == "Bydgoszcz":
        node = 1
    elif miasto == "Gdańsk":
        node = 2
    elif miasto == "Katowice":
        node = 3
    elif miasto == "Kielce":
        node = 4
    elif miasto == "Kraków":
        node = 5
    elif miasto == "Lublin":
        node = 6
    elif miasto == "Łódź":
        node = 7
    elif miasto == "Olsztyn":
        node = 8
    elif miasto == "Opole":
        node = 9
    elif miasto == "Poznań":
        node = 10
    elif miasto == "Rzeszów":
        node = 11
    elif miasto == "Szczecin":
        node = 12
    elif miasto == "Warszawa":
        node = 13
    elif miasto == "Wrocław":
        node = 14
    elif miasto == "Zielona Góra":
        node = 15
    return node


# algorytm greedy tsp
def greedy_tsp(node, list):
    # zamiana nazwy miasta na numer miasta
    if node == -1:
        return
    # algorytm
    visited = []
    path = 0
    for j in range(len(list)):
        current = 1000000
        for i in range(len(list)):
            a = distance(list[node][0], list[node][1], list[i][0], list[i][1])
            if a < current and a != 0 and i not in visited:
                current = a
                next_node = i
        visited.append(node)
        path += a
        node = next_node
    canvas.delete("line")
    odp = int(cost(visited, wspMiast)*1.0682)
    a1.set(odp)
    return visited


# algorytm 2-opt
def twoOpt(visited, wspMiast):
    if visited == None:
        return
    best = visited
    improved = True
    size = len(visited)
    while improved:
        improved = False
        for i in range(1, size-2):
            for j in range(i+1, size):
                if j-i == 1:
                    continue
                new_route = visited[:]
                new_route[i:j] = visited[j-1:i-1:-1]
                if cost(new_route, wspMiast) < cost(best, wspMiast):
                    best = new_route
                    imrpoved = True
        visited = best
        for i in range(len(best)-1):
            m1 = best[i]
            m2 = best[i+1]
    canvas.delete("line")
    odp = int(cost(best, wspMiast)*1.0682)
    a2.set(odp)
    return best


# algorytm genetyczny
class Genetic:
    def __init__(self, pop, pok, krz, mut):
        self.population = pop
        self.generation = pok
        self.cross = krz
        self.mutation = mut

    def algorithm(self, verList, starter):
        if starter == -1:
            return
        verListCopy = verList.copy()
        verListCopy.pop(starter)
        listOfPopulation = []
        half = (len(verListCopy)-1)//2
        for i in range(self.population):
            condition = False
            tmp = []
            while condition is False:
                vertex = random.randint(0, len(verListCopy) - 1)
                if verListCopy[vertex] not in tmp:
                    tmp.append(verListCopy[vertex])
                elif len(verListCopy) == len(tmp):
                    condition = True
            listOfPopulation.append(tmp)

        #################################################
        for k in range(self.generation):
            for i in range(self.cross):
                i0 = random.randint(0, self.population - 1)
                i1 = random.randint(0, self.population - 1)
                while i0 == i1:
                    i1 = random.randint(0, self.population - 1)
                tmp = listOfPopulation[i0][0:half]
                for j in listOfPopulation[i1]:
                    if j not in tmp:
                        tmp.append(j)
                listOfPopulation.append(tmp)

            for i in range(self.mutation):
                i0 = random.randint(0, len(listOfPopulation) - 1)
                x = random.randint(0, len(verListCopy) - 1)
                y = random.randint(0, len(verListCopy) - 1)
                listOfPopulation[i0][x], listOfPopulation[i0][y] = listOfPopulation[i0][y], listOfPopulation[i0][x]

            lenghtsOfPaths = []
            for i in listOfPopulation:
                suma = 0
                for j in range(1, len(i) - 1):
                    suma += distance(i[j - 1][0], i[j - 1][1], i[j][0], i[j][1])
                suma += distance(i[0][0], i[0][1], verList[starter][0],
                        verList[starter][1]) + distance(i[len(verListCopy) - 1][0],
                        i[len(verListCopy) - 1][1], verList[starter][0], verList[starter][1])
                lenghtsOfPaths.append(round(suma, 2))

            sortedList = [x for _, x in sorted(zip(lenghtsOfPaths, listOfPopulation))]
            sortedlenghts = sorted(lenghtsOfPaths)

            listOfPopulation = sortedList
            while len(listOfPopulation) != self.population:
                listOfPopulation.pop()

        #######################################################
        result = [starter]
        for i in listOfPopulation[0]:
            result.append(verList.index(i))
        canvas.delete("line")
        odp = int(cost(result, wspMiast)*1.0682)
        a3.set(odp)
        return result


G = Genetic(200, 200, 3, 3)

# algorytm podziału i ograniczeń
# <editor-fold desc="Algorytm podziału i ograniczeń">
matryca = []

for i in range(len(wspMiast)):
    pomocnicza = []
    for j in range(len(wspMiast)):
        temp = distance(wspMiast[i][0], wspMiast[i][1], wspMiast[j][0], wspMiast[j][1])
        pomocnicza.insert(j, temp)
    matryca.append(pomocnicza)

maxsize = float('inf')


def copyToFinal(curr_path):
    final_path[:N + 1] = curr_path[:]
    final_path[N] = curr_path[0]

def firstMin(adj, i):
    min = maxsize
    for k in range(N):
        if adj[i][k] < min and i != k:
            min = adj[i][k]

    return min


def secondMin(adj, i):
    first, second = maxsize, maxsize
    for j in range(N):
        if i == j:
            continue
        if adj[i][j] <= first:
            second = first
            first = adj[i][j]

        elif (adj[i][j] <= second and
              adj[i][j] != first):
            second = adj[i][j]

    return second


def TSPRec(adj, curr_bound, curr_weight,
           level, curr_path, visited):
    global final_res

    if level == N:

        if adj[curr_path[level - 1]][curr_path[0]] != 0:
            curr_res = curr_weight + adj[curr_path[level - 1]][curr_path[0]]
            if curr_res < final_res:
                copyToFinal(curr_path)
                final_res = curr_res
        return

    for i in range(N):
        if (adj[curr_path[level - 1]][i] != 0 and
                visited[i] == False):
            temp = curr_bound
            curr_weight += adj[curr_path[level - 1]][i]
            if level == 1:
                curr_bound -= ((firstMin(adj, curr_path[level - 1]) +
                                firstMin(adj, i)) / 2)
            else:
                curr_bound -= ((secondMin(adj, curr_path[level - 1]) +
                                firstMin(adj, i)) / 2)
            if curr_bound + curr_weight < final_res:
                curr_path[level] = i
                visited[i] = True
                TSPRec(adj, curr_bound, curr_weight,
                       level + 1, curr_path, visited)

            curr_weight -= adj[curr_path[level - 1]][i]
            curr_bound = temp

            visited = [False] * len(visited)
            for j in range(level):
                if curr_path[j] != -1:
                    visited[curr_path[j]] = True


def TSP(adj):
    curr_bound = 0
    curr_path = [-1] * (N + 1)
    visited = [False] * N
    for i in range(N):
        curr_bound += (firstMin(adj, i) +
                       secondMin(adj, i))
    curr_bound = math.ceil(curr_bound / 2)
    visited[0] = True
    curr_path[0] = 0
    TSPRec(adj, curr_bound, 0, 1, curr_path, visited)


def TSPendgame(city):
    if city == -1:
        return
    else:
        canvas.delete("line")
        odp = int(cost(final_path[:-1], wspMiast)*1.0682)
        a4.set(odp)
        return final_path


N = 16

final_path = [0] * (N + 1)

visited = [False] * N
final_res = maxsize

TSP(matryca)
# </editor-fold>


# root
root = tk.Tk()
root.title('Projekt OK')
root.configure(bg="#323232")

# frames
frame1 = tk.Frame(root, padx=50, pady=215)
frame1.grid(row=0, column=0)
frame1.configure(bg="#323232")

frame2 = tk.Frame(root)
frame2.grid(row=0, column=1)
frame2.configure(bg="#3f3f3f")

frame3 = tk.Frame(root, padx=50, pady=215)
frame3.grid(row=0, column=2)
frame3.configure(bg="#323232")

# frame 2
mapa = ImageTk.PhotoImage(Image.open("map_no_bg.png"))

# CANVAS
canvas = tk.Canvas(frame2, width=600, height=561, bg="#323232", highlightthickness=0)
canvas.grid(row=2, column=0, columnspan=3)
canvas.create_image(300, 280.5, image=mapa)


# frame 1

# LISTA MIAST
wybraneMiasto = tk.StringVar()
wybraneMiasto.set("Wybierz miasto startowe")

miasta = [
    "Białystok", "Bydgoszcz", "Gdańsk", "Katowice",
    "Kielce", "Kraków", "Lublin", "Łódź",
    "Olsztyn", "Opole", "Poznań", "Rzeszów",
    "Szczecin", "Warszawa", "Wrocław", "Zielona Góra"
]

listaMiast = tk.OptionMenu(frame1, wybraneMiasto, *miasta, command=submit)
listaMiast.configure(width=23, bg="#1c94cf", cursor="hand2", highlightthickness=0)
listaMiast.grid(row=0, column=0)


# BUTTONS

button_1alg = tk.Button(frame1, text="Algorytm Zachłanny", command=lambda:
                        draw(greedy_tsp(city_to_number(wybraneMiasto.get()), wspMiast), wspMiast, "green"),
                        bg="#1c94cf", cursor="hand2", width=24)
button_1alg.grid(row=1, column=0)

button_2alg = tk.Button(frame1, text="Algorytm 2-opt", command=lambda:
                        draw(twoOpt(greedy_tsp(city_to_number(wybraneMiasto.get()), wspMiast), wspMiast), wspMiast,
                             "blue"), bg="#1c94cf", cursor="hand2", width=24)
button_2alg.grid(row=2, column=0)

button_3alg = tk.Button(frame1, text="Algorytm Genetyczny", command=lambda:
                        draw(G.algorithm(wspMiast, city_to_number(wybraneMiasto.get())), wspMiast, "red"),
                        bg="#1c94cf", cursor="hand2", width=24)
button_3alg.grid(row=3, column=0)

button_4alg = tk.Button(frame1, text="Algorytm Podziału i Ograniczeń", command=lambda:
                        draw(TSPendgame(city_to_number(wybraneMiasto.get())), wspMiast, "yellow"),
                        bg="#1c94cf", cursor="hand2", width=24)
button_4alg.grid(row=4, column=0)

button_reset = tk.Button(frame1, text="Reset", command=reset, bg="#1c94cf", cursor="hand2", width=24)
button_reset.grid(row=5, column=0)

# frame 3
labelWidth = 24
results = tk.Label(frame3, text="DŁUGOŚCI TRAS W KM", bg="#1c94cf", width=25)
results.grid(row=0, column=0, columnspan=2, pady=1)

alg1 = tk.Label(frame3, text="Alg. Zach.", bg="#1c94cf", width=labelWidth//2)
alg2 = tk.Label(frame3, text="Alg. 2-opt", bg="#1c94cf", width=labelWidth//2)
alg3 = tk.Label(frame3, text="Alg. Gen.", bg="#1c94cf", width=labelWidth//2)
alg4 = tk.Label(frame3, text="Alg. PiO", bg="#1c94cf", width=labelWidth//2)

alg1.grid(row=1, column=0, pady=1)
alg2.grid(row=2, column=0, pady=1)
alg3.grid(row=3, column=0, pady=1)
alg4.grid(row=4, column=0, pady=1)

a1 = tk.IntVar()
a1.set(0)
a2 = tk.IntVar()
a2.set(0)
a3 = tk.IntVar()
a3.set(0)
a4 = tk.IntVar()
a4.set(0)

alg1_res = tk.Label(frame3, textvariable=a1, bg="#1c94cf", width=labelWidth//2)
alg2_res = tk.Label(frame3, textvariable=a2, bg="#1c94cf", width=labelWidth//2)
alg3_res = tk.Label(frame3, textvariable=a3, bg="#1c94cf", width=labelWidth//2)
alg4_res = tk.Label(frame3, textvariable=a4, bg="#1c94cf", width=labelWidth//2)

alg1_res.grid(row=1, column=1, padx=1, pady=1)
alg2_res.grid(row=2, column=1, padx=1, pady=1)
alg3_res.grid(row=3, column=1, padx=1, pady=1)
alg4_res.grid(row=4, column=1, padx=1, pady=1)

root.mainloop()
