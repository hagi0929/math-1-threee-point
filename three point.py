import fractions
import decimal

class three_point:
    def __init__(self,*coordinate_input):
        self.coordinate_list = []
        for i in coordinate_input:
            local_raw_coordinate_dictonary = {}
            xy_seperated_list = i.replace(' ','').replace('(','').replace(')','').split(',')
            local_raw_coordinate_dictonary['x'] = int(xy_seperated_list[0])
            local_raw_coordinate_dictonary['y'] = int(xy_seperated_list[1])
            self.coordinate_list.append(local_raw_coordinate_dictonary)
    def solve(self):
        if len(self.coordinate_list) == 3:
            equation_list = [] #final answer
            solver_list = [] # for example -3A-2B+C=-13
            for coordinate in self.coordinate_list:
                solver_dictonary = {}
                solver_dictonary['value'] = -((coordinate['x']**2)+(coordinate['y']**2))
                solver_dictonary['A'] = coordinate['x']
                solver_dictonary['B'] = coordinate['y']
                solver_dictonary['C'] = 1
                solver_list.append(solver_dictonary)
            subtrancted_list = [] # for example 7A-7B=-84
            for i,j in enumerate([(1+foo)%3 for foo in range(3)]): # subtract all the equation i,j : 0,1 : 1,2 : 2,0
                solver_dictonary = {}
                solver_dictonary['value'] = solver_list[i]['value'] - solver_list[j]['value']
                solver_dictonary['A'] = solver_list[i]['A'] - solver_list[j]['A']
                solver_dictonary['B'] = solver_list[i]['B'] - solver_list[j]['B']
                solver_dictonary['C'] = solver_list[i]['C'] - solver_list[j]['C']
                subtrancted_list.append(solver_dictonary)
            diffrence_list = []
            for i, j in enumerate([(1 + foo) % 3 for foo in range(3)]):
                solver_dictonary = {}

                constant_dictionary = {'B': fractions.Fraction(decimal.Decimal(subtrancted_list[i]['A']) / decimal.Decimal(subtrancted_list[j]['A'])),'A':fractions.Fraction(decimal.Decimal(subtrancted_list[i]['B']) / decimal.Decimal(subtrancted_list[j]['B']))}
                for AB,constant in constant_dictionary.items():
                    AB_diffrence = subtrancted_list[i][AB] - subtrancted_list[j][AB] * constant
                    value_diffrence = subtrancted_list[i]['value'] - subtrancted_list[j]['value'] * constant
                    solver_dictonary[AB] = value_diffrence/AB_diffrence
                    diffrence_list.append(solver_dictonary)
            ope=["","",""]
            abc=['A','B','C']
            for original_solver in solver_list:
                for AB_value in diffrence_list:
                    AB_value['C'] = original_solver['value']-(AB_value['A']*original_solver['A']+AB_value['B']*original_solver['B'])
                for i in range(3):
                    if AB_value[abc[i]] >= 0:
                        ope[i]="+"
                equation_list.append("x^2+y^2{}{}x{}{}y{}{} = 0".format(ope[0],float(AB_value['A']),ope[1],float(AB_value['B']),ope[2],float(AB_value['C'])))
            if all(x==equation_list[0] for x in equation_list):
                print(equation_list[0])
            else:
                print("warning!! there might be error\n{}".format(equation_list))
        else:
            print("there are  {} coordinates \n we need exantly 3 coordinates stupid!".format(len(self.coordinate_list)))
def try_shit():
    while True:
        try:
            input_Shit = input("3 coordinates of the circle: ")
            if "fuck off" in input_Shit or "exit" in input_Shit or "go away" in input_Shit:
                break
            else:
                list_mamamo = input_Shit.split()
                a = three_point(list_mamamo[0],list_mamamo[1],list_mamamo[2])
                a.solve()
        except:
            print("unknown error--!!")
print("the format should be only (x1,y1) (x2,y2) (x3,y3) #only space between points")
try_shit()