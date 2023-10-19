from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    """
        A Car Make class that contains structure to store Car Make data
    """
    name = models.CharField(null=False, max_length=100, default="Make name")
    description = models.CharField(max_length=500)

    def __str__(self):
        return "Name: " + self.name + "," + \
            "Description :" + self.description


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    """
        A Car Model class that contains structure to store data about a car model
    """
    SEDAN = "sedan"
    SUV = "suv"
    WAGON = 'wagon'
    TRUCK = 'truck'

    CAR_TYPE_CHOICES = [
        (SEDAN, "Sedan"),
        (SUV, "Suv"),
        (WAGON, "Wagon"),
        (TRUCK, "Truck")
    ]
    car_make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()
    name = models.CharField(null=False, max_length=100, default="Model Name")
    car_type = models.CharField(null=False, max_length=100, default="Sedan", choices=CAR_TYPE_CHOICES)
    year = models.DateField(null=True)

    def __str__(self):
        return "Car Make: " + self.car_make + "," + \
            "Dealer Id: " + self.dealer_id + "," + \
                "Model Name: " + self.name + "," + \
                    "Type: " + self.car_type + "," + \
                        "Year: " + self.year



# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
