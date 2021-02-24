import pickle
import pandas as pd
import os
from django.db import connection
from django.conf import settings

def predict(requirements):
    feature_list = {}
    prediction_model = {}
    for platform in requirements.keys():
        model_name = platform + '.sav'
        path = os.path.join(settings.BASE_DIR, 'models', model_name)
        loaded_model = pickle.load(open(path, 'rb'))
        feature_list[platform] = loaded_model.feature_names
        prediction_model[platform] = loaded_model

    designation_group = {}
    for platform in requirements.keys():
        group = {}
        req_modules = list(requirements[platform])
        while req_modules:
            model_input = []
            for element in feature_list[platform]:
                if element in req_modules:
                    model_input.append(1)
                else:
                    model_input.append(0)
                    
            Predicted_Designation = prediction_model[platform].predict([model_input])
            # print(Predicted_Designation[0])
            
            query = '''SELECT
                        webapp_designation.designation AS Employee_Designation,
                        webapp_modules.module AS Employee_Module,
                        webapp_platform.platform AS Employee_Platform
                    FROM
                        webapp_designation
                        JOIN webapp_employeemodules ON webapp_employeemodules.designation_id = webapp_designation.id
                        JOIN webapp_employeemodules_module ON webapp_employeemodules_module.employeemodules_id = webapp_employeemodules.id
                        JOIN webapp_employeemodules_platform ON webapp_employeemodules_platform.employeemodules_id = webapp_employeemodules_module.employeemodules_id
                        JOIN webapp_modules ON webapp_modules.id = webapp_employeemodules_module.modules_id
                        JOIN webapp_platform ON webapp_platform.id = webapp_employeemodules_platform.platform_id
                    WHERE Employee_Designation = :Designation;'''
            Predicted_Designation_df = pd.read_sql_query(query,connection, params={"Designation": Predicted_Designation[0]})
            
            Predicted_Designation_modules = Predicted_Designation_df.Employee_Module.tolist()
            Designation_modules_required = []
            for module in Predicted_Designation_modules:
                if module in req_modules:
                    Designation_modules_required.append(module)
                    req_modules.remove(module)
                else:
                    pass
            group[Predicted_Designation[0]] = Designation_modules_required
        designation_group[platform] = group

    for platform, group in designation_group.items():
        print("\n\tPlatform:", platform)
        for designation, modules in group.items():
            print(designation,modules)
        print("\n")
    
    return designation_group