import pickle
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
Year = input("What is the year? ")
Present_Price = input("What is the current price (in '100,000)? ")
Kms_Driven2 = input("How many kilometres has been driven? ")
Owner = input("How many people had the ownership of the car previously? ")

Fuel_Type_Petrol = 0
Fuel_Type_Diesel = 0 
Fuel_Type = input("Does it use petrol or diesel (1 for petrol, 2 for diesel)? ")
if(Fuel_Type == 1):
    Fuel_Type_Petrol=1
else:
    Fuel_Type_Diesel=1

Seller_Type_Individual = 0
Seller_Type = input("Are you an Individual or a Dealer (1 for Individual, 2 for Dealer)? ")
if(Seller_Type == 1):
    Seller_Type_Individual=1

Transmission_Manual = 0
Transmission = input("What is the transmission type of the car (1 for Manual, 2 for Automatic)? ")
if(Transmission == 1):
    Transmission_Manual=1

prediction=model.predict([[Present_Price,Kms_Driven2,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]])
output=round(prediction[0],2)
print(output)