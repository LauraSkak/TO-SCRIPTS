#Exercise 1
class Vehicle:
    def __init__(self, name, seats, trunk_space):
        self.name = name
        self.seats = seats
        self.trunk_space = trunk_space
        #Exercise 5
        self.fuel = 'gasoline'

    #Exercise 2

    def __str__(self):
        return self.name
    
    #Exercise 3

    def at_capacity(self, passengers, suitcases):
        if passengers > self.seats:
            return True
        elif suitcases >= self.trunk_space + (self.seats-passengers):
            return True
        else:
            return False


#car = Vehicle("Dodge", 2, 1)
#print(f'The {car.name} has {car.seats} seats and {car.trunk_space} units of trunk space')

#car = Vehicle("Jeep", 4, 2)
#print(car)

car = Vehicle("Volvo", 4, 3)
print(f'It is {car.at_capacity(4, 2)} that the {car.name} is at/over capacity')

#Exercise 4
class Bus(Vehicle):
    #exercise 5 kan også skrives udenfor init:
    #fuel='diesel'

    #Behøver ikke at definere dette, da det bare kan komme fra Vehicle)
    def __init__(self, name, seats, trunk_space):
        self.name = name
        self.seats = seats
        self.trunk_space = trunk_space
        #Exercise 5
        self.fuel = 'diesel'
    
    def at_capacity(self, passengers, suitcases):
        if passengers > self.seats:
            return True
        elif suitcases >= self.seats:
            return True
        return False
        
#school_bus = Bus("School bus", 22, 10)
#print(f'The {school_bus.name} has {school_bus.seats} seats and {school_bus.trunk_space} units of trunk space')
#print(f'It is {school_bus.at_capacity(22, 11)} that the {school_bus.name} is at/over capacity')

#tour_bus = Bus("Dodge", 30, 20)
#convertible =  Vehicle("Saab", 4, 1)
#print(f'The {tour_bus.name} uses {tour_bus.fuel}')
#print(f'The {convertible.name} uses {convertible.fuel}')

#Exercise 6
class Truck(Vehicle):
    def __init__(self, name, passengers, trunk_units, trailer_units):
        super().__init__(name, passengers, trunk_units)
        self.trailer_units =  trailer_units

#sixteen_wheeler = Truck('Man', 2, 2, 542)
#print(sixteen_wheeler)

#Exercise 7
class AutoTransport(Vehicle):
    def __init__(self, name, passengers, trunk_units):
        super().__init__(name, passengers, trunk_units)
        self.loaded_cars = []

    def __str__(self):
        return f"{self.name} with: {', '.join(map(str, self.loaded_cars))}"
    
    def load(self, car):
        self.loaded_cars.append(car.name)

auto_trans = AutoTransport('Man', 2, 2)
#print(auto_trans)
auto_trans.load(Vehicle('Mustang', 4, 1))
auto_trans.load(Vehicle('Charger', 4, 1))
auto_trans.load(Vehicle('Corvette', 4, 1))
auto_trans.load(Vehicle('Challenger', 4, 1))
#print(auto_trans)

#Exercise 8
class DNA:
    def __init__(self, string):
        self.string = string
    
    def count_nucleotides(self):
        nucleotides_dict={'A':0, 'T':0, 'C':0, 'G':0}
        for n in self.string:
            nucleotides_dict[n]+=1
        return nucleotides_dict
    
    def GC_content(self):
        count_dict=self.count_nucleotides()
        GC_count=count_dict['C']+count_dict['G']
        count_sum=count_dict['C']+count_dict['G']+count_dict['A']+count_dict['T']
        return GC_count/count_sum
    
    def codons(self):
        codon_list=[]
        for i in range(0,len(self.string)-2,3):
            codon_list.append(self.string[i:i+3])
        return codon_list

    def protein_seq(self):
        CODON_MAP = {'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
             'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 
             'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*', 
             'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W', 
             'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
             'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 
             'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 
             'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 
             'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 
             'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 
             'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 
             'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 
             'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 
             'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 
             'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 
             'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}
        
        protein=''
        codon_list=self.codons()
        for codon in codon_list:
            protein+=CODON_MAP[codon]
        return protein
    
    def reverse_complement(self):
        reverse_string=''
        complement_dict={'A':'T','T':'A', 'C':'G', 'G':'C'}
        for i in range(len(self.string)-1,-1,-1):
            reverse_string+=complement_dict[self.string[i]]
        return reverse_string

#class RNA(DNA):
    # #def __init__(self, string):
    # #    if 'T' in string:
    #         self.DNA=string
    #     else:
    #         DNA_string=''
    #         for base in string:
                 
    #         self.DNA=
    #     return None
    
    # def reverse_complemenent(self):
    #     reverse_string=''
    #     complement_dict={'A':'U','U':'A', 'C':'G', 'G':'C'}
    #     for i in range(len(self.string)-1,-1,-1):
    #         reverse_string+=complement_dict[self.string[i]]
    #     return reverse_string
    
    # #def codons(self):



string=DNA('ATGGGCTTGACT')

#print(string.count_nucleotides())
#print(string.GC_content())
#print(string.codons())
#print(string.protein_seq())
#print(string.reverse_complement())



