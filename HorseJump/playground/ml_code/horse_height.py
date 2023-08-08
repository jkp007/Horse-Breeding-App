import pandas as pd

class horse_height:

    horse_name = pd.read_csv('/workspaces/Horse-Breeding-App/HorseJump/playground/ml_code/Horse Data.csv', skipinitialspace = True)
    horse_name.columns = horse_name.columns.str.replace(' ', '')
    horse_name.columns = horse_name.columns.str.strip()

    horse_name['Sire'] = horse_name['Sire'].str.replace(' ', '')
    horse_name['Dam'] = horse_name['Dam'].str.replace(' ', '')

    mean_height_by_horse_male = horse_name.groupby('Sire')["Sire'slevel"].mean()
    mean_height_by_horse_female = horse_name.groupby('Dam')["Dam'slevel"].mean()

    male_horse_height = mean_height_by_horse_male.to_dict()
    female_horse_height = mean_height_by_horse_female.to_dict()
