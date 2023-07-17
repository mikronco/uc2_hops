import numpy as np
import pandas as pd

def build_win_feature(dataset, windows, mode, window_name):
    
    features = pd.DataFrame()
    value_mean = dataset.mean()
    dataset = pd.DataFrame(dataset)
    
    for column in dataset:
        i = 0

        for win in windows:
            
            name = column + ' ' + str(window_name[i])
            i = i + 1
            # Rolling Sum for precipitation or conflict / Rolling mean for the rest
            
            if mode == 'sum':
                dataset[name] = dataset[column].rolling(win).sum()

            if mode == 'mean':
                dataset[name]= dataset[column].rolling(win).mean()
                          
    return dataset


def build_lag_feature(dataset, lags):
    
    features = pd.DataFrame()
    dataset = pd.DataFrame(dataset)
    
    for column in dataset:
        i = 0

        for lag in lags:
            name = column + ' ' + 'lag' + str(lags[i])
            i = i + 1
            lagged_column = dataset[column].shift(lag).rename(name)
            dataset = pd.concat([dataset, lagged_column], axis=1)
            # dataset[name] = dataset[column].shift(lag)
                                             
    return dataset



def market_sub(district, market_data, full_data):
          
            
        if district == 'Baidoa':
            market_data['Vegetable Oil Price'][market_data['Vegetable Oil Price'] > 100000.0] = None
            
        if district == 'Baardheere':

            replace_from = Somalia_IDP_Database[Somalia_IDP_Database['District'] == 'Diinsoor'] 
            replace_from.index = replace_from.Date
            market_data['Water Drum Price'] = replace_from['Water Drum Price']        
        
        if district == 'Qoryooley':
            replace_from = Somalia_IDP_Database[Somalia_IDP_Database['District'] == 'Wanla Weyn'] 
            replace_from.index = replace_from.Date
            
            market_data['Cattle Price'] = replace_from['Cattle Price']
            market_data['Camel Price'] = replace_from['Camel Price']
            
            replace_from = Somalia_IDP_Database[Somalia_IDP_Database['District'] == 'Marka'] 
            replace_from.index = replace_from.Date
            
            market_data['SomaliShillingToUSD'] = replace_from['SomaliShillingToUSD']
            market_data['Cowpeas Price'] = replace_from['Cowpeas Price']
            market_data['Water Drum Price'] = replace_from['Water Drum Price']    
            
        
        if district == 'Buur Hakaba':
            
            replace_from = Somalia_IDP_Database[Somalia_IDP_Database['District'] == 'Marka'] 
            replace_from.index = replace_from.Date
            
            market_data['SomaliShillingToUSD'] = replace_from['SomaliShillingToUSD']
            market_data['Cowpeas Price'] = replace_from['Cowpeas Price']
            market_data['Water Drum Price'] = replace_from['Water Drum Price']
            market_data['Vegetable Oil Price'] = replace_from['Vegetable Oil Price']
            
            
            replace_from = Somalia_IDP_Database[Somalia_IDP_Database['District'] == 'Baidoa'] 
            replace_from.index = replace_from.Date
            
            market_data['Cattle Price'] = replace_from['Cattle Price']
            market_data['Camel Price'] = replace_from['Camel Price']
            
            
        if district == 'Afgooye':
            
            replace_from = Somalia_IDP_Database[Somalia_IDP_Database['District'] == 'Balcad'] 
            replace_from.index = replace_from.Date
            
            market_data['Red Sorghum Price'] = replace_from['Red Sorghum Price']
            market['Vegetable Oil Price'] = replace_from['Vegetable Oil Price']
            market_data['Goat Price'] = replace_from['Goat Price']
            market_data['Sugar Price'] = replace_from['Sugar Price']
            market_data['Camel Milk Price'] = replace_from['Camel Milk Price']
            market_data['Tea Leaves Price'] = replace_from['Tea Leaves Price']
            market_data['Vegetable Oil Price'][market_data['Vegetable Oil Price'] > 100000.0] = None       
            
            replace_from = Somalia_IDP_Database[Somalia_IDP_Database['District'] == 'Marka'] 
            replace_from.index = replace_from.Date
            market_data['SomaliShillingToUSD'] = replace_from['SomaliShillingToUSD']
            market_data['Water Drum Price'] = replace_from['Water Drum Price']
            market_data['Cowpeas Price'] = replace_from['Cowpeas Price']
            
            replace_from = Somalia_IDP_Database[Somalia_IDP_Database['District'] == 'Wanla Weyn'] 
            replace_from.index = replace_from.Date
            
            market_data['Cattle Price'] = replace_from['Cattle Price']
            market_data['Camel Price'] = replace_from['Camel Price']      
            
        
        if district == 'Garbahaarey':
            replace_from = Somalia_IDP_Database[Somalia_IDP_Database['District'] == 'Qansax Dheere'] 
            replace_from.index = replace_from.Date
            
            market_data['Cattle Price'] = replace_from['Cattle Price']
            market_data['Camel Price'] = replace_from['Camel Price']
            market_data['Cowpeas Price'] = replace_from['Cowpeas Price']
            market_data['Water Drum Price'] = replace_from['Water Drum Price']
        

        return market_data