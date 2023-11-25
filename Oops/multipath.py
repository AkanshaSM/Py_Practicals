class LandVehicle:
    def __init__(self,name):
        self.name=name
    def drive(self):
        print("Simulation of Land Vehicle"+self.name)
    
class WaterVehicle:
    def __init__(self,name):
        self.name=name
    def sail(self):
        print("Simulation of water vehicle"+self.name)

class AmphibiousVehicle(LandVehicle,WaterVehicle):
    
    def __init__(self,name,propulsion_type):
        LandVehicle.__init__(self,name)
        WaterVehicle.__init__(self,name)
        self.propulsion_type=propulsion_type

    def travel(self):
        print(f"Simulation of {self.name} with propulsion {self.propulsion_type}")
        
obj=AmphibiousVehicle('HondaSM','Wheels')
obj.travel()

