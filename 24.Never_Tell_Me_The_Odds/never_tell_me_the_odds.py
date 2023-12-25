from sympy import symbols, Symbol, Eq, solve

class Hail:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.vx = int(vx)
        self.vy = int(vy)
        self.vz = int(vz)
    
    def display(self):
        print(self.x, self.y, self.z, self.vx, self.vy, self.vz)

def get_puzzle(path):
    with open(path) as file:
        return parse_input(file)
    
def parse_input(file):
    HAIL = []
    for line in file:
        positions, velocities = line.strip().split(' @ ')
        x, y, z = positions.split(', ')
        vx, vy, vz = velocities.split(', ')
        HAIL.append(Hail(x, y, z, vx, vy, vz))
    return HAIL

def get_total_intersections(HAIL, start, stop):
    total_hails = len(HAIL)
    total_intersections = 0
    for i in range(total_hails):
        for j in range(i + 1, total_hails):
            intersection = find_intersections(HAIL[i], HAIL[j])
            if intersection is None: continue
            x, y = intersection
            if start <= x <= stop and start <= y <= stop:
                # HAIL[i].display()
                # HAIL[j].display()
                total_intersections += 1
    return total_intersections

def find_intersections(hail1, hail2):
    '''2 linear equations -> at1 + bt2 + c = 0
    # coeffs => a1,b1,c1 a2,b2,c2'''
    a1, b1, c1 = hail1.vx, -hail2.vx, hail1.x - hail2.x
    a2, b2, c2 = hail1.vy, -hail2.vy, hail1.y - hail2.y
    solution = solve_equations(a1, b1, c1, a2, b2, c2)
    if not solution: return
    t1, t2 = solution.values()
    if t1 < 0 or t2 < 0: return
    x, y = hail1.x + hail1.vx*t1, hail1.y + hail1.vy*t1
    return x, y
    

def solve_equations(a1, b1, c1, a2, b2, c2):
    t1, t2 = symbols('t1,t2')
    eq1 = Eq((a1*t1+b1*t2), -c1)
    eq2 = Eq((a2*t1+b2*t2), -c2)
    return solve((eq1, eq2), (t1, t2))
    
def get_rock_position(HAIL):
    x,y,z,vx,vy,vz = symbols('x,y,z,vx,vy,vz')
    equations = []
    time_symbols = []
    #Finding intersection of first 3 hailstones
    for index, hail in enumerate(HAIL[:3]):
        t = Symbol('t'+str(index))
        eqx = x + vx*t - (hail.x + hail.vx*t)
        eqy = y + vy*t - (hail.y + hail.vy*t)
        eqz = z + vz*t - (hail.z + hail.vz*t)

        equations.extend([eqx, eqy, eqz])
        time_symbols.append(t)
    solution = solve(equations,*([x,y,z,vx,vy,vz]+time_symbols))
    return sum(solution[0][:3])
    
path = "24.Never_Tell_Me_The_Odds\input.txt"
HAIL = get_puzzle(path)
# for hail in HAIL:
#     hail.display()
#Sample input
# print(get_total_intersections(HAIL, start=7, stop=27))

#Part 1
print(get_total_intersections(HAIL, start=200000000000000, stop=400000000000000))

#Part 2
print(get_rock_position(HAIL))

'''
Part 1 Working
Equation in 2 vars
x
19 - 2t1 = 18 - t2
1 = 2t1 - t2
-2t1 + t2 + (19 - 18) = 0
y
13 + t1 = 19 - t2
t1 + t2 = 6
Solving eqns 2t1 - t2 = 1, t1 + t2 = 6
t1 = 2.333, t2 = 3.667
19 - 2t1 = 14.333 = 18 - t2
=> 
19, 13 : -2,1
20, 19 : 1, -5
19 - 2t1 = 20 + t2 => 2t1 + t2 = -1
13 + t1 = 19 - 5t2 => t1 + 5t2 = 6
=>
18 - t1 = 20 - 2t2 => t1 - 2t2 = -2
19 - t1 = 25 - 2t2 => t1 - 2t2 = -6
'''