class vehicle:
    
     # constructor,price: The price of the vehicle.color: The color of the vehicle.tank_capacity: The capacity of the vehicle's fuel tank in gallons.miles_range: The range of the vehicle in miles.
    def __init__(self,color,tank_capacity,miles_range,price):
        self.color= color
        self.tank_capacity=tank_capacity
        self.miles_range=miles_range
        self.price=price
    #public function
    def calculate_mpg(self)-> float:
        """
        Calculate the miles per gallon(mpg) of the vehicle.
        Returns:
            float: The miles per gallon(mpg) of the vehicle. 
        """
        if self.tank_capacity==0:
            return 0
        else:
            return self.miles_range / self.tank_capacity
    
    def user_car_input(self):
        while True:
            car_color=input("Enter the color of the car:\n")
            try:
                miles=float(input("Enter the mile of the car:\n"))
                tank=float(input("Enter the tank capacity of the car:\n"))
                car_price=float(input("Enter the price of the car:\n"))
            except:
                print("Invalid input, please enter integers for miles, price and tank capacity")
                return
            self.color=car_color
            self.miles_range= miles
            self.tank_capacity=tank
            self.price=car_price
            
            line= "-"*60
            print(f"\033[31m{line}\033[0m\n") 

            print("\033[33mEntered Vehicle information:\033[0m") 
            print(f'Color of the car:{car_color}\nMiles_range:{miles}\ntank capacity:{tank}\nPrice of the vehicle is:{car_price}')
            return f'miles range:{miles} / tank capactiy:{tank} = {self.calculate_mpg()}\n'
            

if __name__=="__main__":
    obj=vehicle("white",18,800,25000)
    print(obj.calculate_mpg())
    print(obj.user_car_input())
   

         