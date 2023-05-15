loop_value = 0					
while loop_value == 0:			
    atomic_number_mass = { 		        # dictionary
    "H" : [1, 1.007],	
    "He" : [2, 4.003],	
    "Li" : [3, 6.941],
    "Be" : [4, 9.012],
    "B" : [5, 10.812],
    "C" : [6, 12.011],
    "N" : [7, 14.007],
    "O" : [8, 15.999],
    "F" : [9, 18.998],
    "Ne" : [10, 20.18],
    "Na" : [11, 22.99],
    "Mg" : [12, 24.305],
    "Al" : [13, 26.982],
    "Si" : [14, 28.086],
    "P" : [15, 30.974],
    "S" : [16, 32.066],
    "Cl" : [17, 35.453],
    "Ar" : [18, 39.948],
    "K" : [19, 39.098],
    "Ca" : [20, 40.078],
    "Sc" : [21, 44.956],
    "Ti" : [22, 47.867],
    "V" : [23, 50.942],
    "Cr" : [24, 51.996],
    "Mn" : [25, 54.938],
    "Fe" : [26, 55.845],
    "Co" : [27, 58.933],
    "Ni" : [28, 58.693],
    "Cu" : [29, 63.546],
    "Zn" : [30, 65.382],
    "Ga" : [31, 69.723],
    "Ge" : [32, 72.631],
    "As" : [33, 74.922],
    "Se" : [34, 78.963],
    "Br" : [35, 79.904],
    "Kr" : [36, 83.798],
    "Rb" : [37, 85.468],
    "Sr" : [38, 87.621],
    "Y" : [39, 88.906],
    "Zr" : [40, 91.224],
    "Nb" : [41, 92.906],
    "Mo" : [42, 95.962],
    "Tc" : [43, 98],
    "Ru" : [44, 101.072],
    "Rh" : [45, 102.906],
    "Pd" : [46, 106.421],
    "Ag" : [47, 107.868],
    "Cd" : [48, 112.412],
    "In" : [49, 114.818],
    "Sn" : [50, 118.711],
    "Sb" : [51, 121.76],
    "Te" : [52, 127.603],
    "I" : [53, 126.904],
    "Xe" : [54, 131.294],
    "Cs" : [55, 132.905],
    "Ba" : [56, 137.328],
    "La" : [57, 138.905],
    "Ce" : [58, 140.116],
    "Pr" : [59, 140.908],
    "Nd" : [60, 144.242],
    "Pm" : [61, 145],
    "Sm" : [62, 150.362],
    "Eu" : [63, 151.964],
    "Gd" : [64, 157.253],
    "Tb" : [65, 158.925],
    "Dy" : [66, 162.5],
    "Ho" : [67, 164.93],
    "Er" : [68, 167.259],
    "Tm" : [69, 168.934],
    "Yb" : [70, 173.055],
    "Lu" : [71, 174.967],
    "Hf" : [72, 178.492],
    "Ta" : [73, 180.948],
    "W" : [74, 183.841],
    "Re" : [75, 186.207],
    "Os" : [76, 190.233],
    "Ir" : [77, 192.217],
    "Pt" : [78, 195.085],
    "Au" : [79, 196.967],
    "Hg" : [80, 200.592],
    "Tl" : [81, 204.383],
    "Pb" : [82, 207.21],
    "Bi" : [83, 208.98],
    "Po" : [84, 209],
    "At" : [85, 210],
    "Rn" : [86, 222],
    "Fr" : [87, 223],
    "Ra" : [88, 226],
    "Ac" : [89, 227],
    "Th" : [90, 232.038],
    "Pa" : [91, 231.036],
    "U" : [92, 238.029],
    "Np" : [93, 237],
    "Pu" : [94, 244],
    "Am" : [95, 243],
    "Cm" : [96, 247],
    "Bk" : [97, 247],
    "Cf" : [98, 251],
    "Es" : [99, 252],
    "Fm" : [100, 257],
    "Md" : [101, 258],
    "No" : [102, 259],
    "Lr" : [103, 266],
    "Rf" : [104, 267],
    "Db" : [105, 268],
    "Sg" : [106, 269],
    "Bh" : [107, 270],
    "Hs" : [108, 277],
    "Mt" : [109, 278],
    "Ds" : [110, 281],
    "Rg" : [111, 282],
    "Cn" : [112, 285],
    "Nh" : [113, 286],
    "Fl" : [114, 289],
    "Mc" : [115, 290],
    "Lv" : [116, 293],
    "Ts" : [117, 294],
    "Og" : [118, 294]
    }

    x = input("\nEnter molecular formula:  ")
    import re				
    y = re.findall('[a-zA-Z][^A-Z]*', x)            # This separates the molecular formula by Uppercase.
                                                    # It leads to create key values. 
    z = [re.split(r'(\d+)', s)[0:2] for s in (y)]
    n = 0                                           # for scrutinizing each atom one by one
    molar_mass = 0
    while len(z) > n:	
        formula = z[n]
        atom = formula[0]
        if len(formula) > 1:
            c = int(formula[1])
        else:
            c = 1
        d = atomic_number_mass.get(atom)[1]
        molar_mass += (c * d)
        n += 1	                                    # go to next atom
    print("Molar mass of ", x, "is ", round(molar_mass, 3))

    n = 0   
    while len(z) > n:
        for formula in (z[n]):
            a = formula.split(',')	            # conversion to list
            b = " ".join(str(x) for x in a)
            try:
                c = float(b)
            except ValueError:	                    # Error handler str to float
                atom = str(b)
                c = 1
                d = atomic_number_mass.get(atom)[1]
        elemental_mass =(c*d)
        elemental_mass = (elemental_mass*100/molar_mass)
        print("Atomic mass % of ", atom, "is ", round(elemental_mass,3))
        n = n + 1	
        c = 1; d = 0
