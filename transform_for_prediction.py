#import libraries
import pandas as pd
import numpy as np
import pickle

#define function to take user input
def transform_for_prediction(name,year,avg_price,kilometers,fuel,seller,transmission,owners):
    
    #initialize a 1x106 dataframe of zeros
     record = pd.DataFrame(np.zeros(106)).T
    
    #all car names
     car_names = ['800', 'Activa 3G', 'Activa 4G', 'Alto 800', 'Alto K10', 'Amaze',
            'Bajaj  Ct 100', 'Bajaj Avenger 150', 'Bajaj Avenger 150 Street',
            'Bajaj Avenger 220', 'Bajaj Avenger 220 Dtsi',
            'Bajaj Avenger Street 220', 'Bajaj Discover 100',
            'Bajaj Discover 125', 'Bajaj Dominar 400', 'Bajaj Pulsar  Ns 200',
            'Bajaj Pulsar 135 Ls', 'Bajaj Pulsar 150', 'Bajaj Pulsar 220 F',
            'Bajaj Pulsar Ns 200', 'Bajaj Pulsar Rs200', 'Baleno', 'Brio',
            'Camry', 'Ciaz', 'City', 'Corolla', 'Corolla Altis', 'Creta',
            'Dzire', 'Elantra', 'Eon', 'Ertiga', 'Etios Cross', 'Etios G',
            'Etios Gd', 'Etios Liva', 'Fortuner', 'Grand I10',
            'Hero  Cbz Xtreme', 'Hero  Ignitor Disc', 'Hero Extreme',
            'Hero Glamour', 'Hero Honda Cbz Extreme', 'Hero Honda Passion Pro',
            'Hero Hunk', 'Hero Passion Pro', 'Hero Passion X Pro',
            'Hero Splender Ismart', 'Hero Splender Plus',
            'Hero Super Splendor', 'Honda Activa 125', 'Honda Activa 4G',
            'Honda Cb Hornet 160R', 'Honda Cb Shine', 'Honda Cb Trigger',
            'Honda Cb Twister', 'Honda Cb Unicorn', 'Honda Cbr 150',
            'Honda Dream Yuga ', 'Honda Karizma', 'Hyosung Gt250R', 'I10',
            'I20', 'Ignis', 'Innova', 'Jazz', 'Ktm 390 Duke ', 'Ktm Rc200',
            'Ktm Rc390', 'Land Cruiser', 'Mahindra Mojo Xt300', 'Omni', 'Ritz',
            'Royal Enfield Bullet 350', 'Royal Enfield Classic 350',
            'Royal Enfield Classic 500', 'Royal Enfield Thunder 350',
            'Royal Enfield Thunder 500', 'S Cross', 'Suzuki Access 125',
            'Swift', 'Sx4', 'Tvs Apache Rtr 160', 'Tvs Apache Rtr 180',
            'Tvs Jupyter', 'Tvs Sport ', 'Tvs Wego', 'Um Renegade Mojave',
            'Verna', 'Vitara Brezza', 'Wagon R', 'Xcent', 'Yamaha Fazer ',
            'Yamaha Fz  V 2.0', 'Yamaha Fz 16', 'Yamaha Fz S ',
            'Yamaha Fz S V 2.0']
    
    #initialize feature_names with numerical variables
     feature_names = ['Year','Present_Price','Kms_Driven']
     
    #numerical variables array
     numerical = feature_names
    
    ##reminder: drop_first was enabled in pd.get_dummies so some variables are "missing"
    
    #for loop to generate car names (Car_Name_1 to Car_Name_97) and append to feature_names array
     for i in range(1,98):
         
         feature_names = np.append(feature_names,'Car_Name_{}'.format(i))
     
    #append remaining variables to feature_names
     feature_names = np.append(feature_names,['Fuel_Type_1','Fuel_Type_2',
                                              'Seller_Type_1','Transmission_1',
                                              'Owner_1','Owner_3'])
    #assign column names to record dataframe
     record.columns = feature_names
    
    #convert all entries to integers
     record = record.astype('int')
    
    #insert year
     record['Year'] = year
    
    #make year an integer
     record['Year'] = int(record['Year'])
    
    #insert avg_price
     record['Present_Price'] = avg_price
    
    #make avg_price a float
     record['Present_Price'] = float(record['Present_Price'])
    
    #insert kilometers
     record['Kms_Driven'] = kilometers
     
    #make kilometers a float
     record['Kms_Driven'] = float(record['Kms_Driven'])
    
    #insert 1 for type of fuel
     if fuel == 'Diesel':
         record['Fuel_Type_1'] = 1
     elif fuel == 'Petrol':
         record['Fuel_Type_2'] = 1
    
    #insert 1 for type of seller
     if seller == 'Individual':
         record['Seller_Type_1'] = 1
    
    #insert 1 for type of transmission
     if transmission == 'Manual':
         record['Transmission_1'] = 1
    
    #insert 1 for number of owners
     if owners == '1':
         record['Owner_1'] = 1
     elif owners == '3':
         record['Owner_3'] = 1
    
    #generate car name based on user input
     car_index = car_names.index(name)
     car_name = 'Car_Name_{}'.format(car_index)
    
    #insert 1 for car name
     if car_name != 'Car_Name_0':
         record[car_name] = 1
    
    #load fitted scaler pickle
     scaler = pickle.load(open('scaler.pkl', 'rb'))
    
    #scale the numerical entries of the record
     record[numerical] = scaler.transform(record[numerical])
    
    #output record
     return record
