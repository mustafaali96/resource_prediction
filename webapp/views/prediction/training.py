import pickle
import pandas as pd
import sqlite3
import os
from django.db import connection
from django.conf import settings
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

def train():
    query = '''SELECT
                    webapp_platform.platform AS Platform,
                    webapp_modules.module AS Module,
                    webapp_designation.designation AS EmployeeDesignation
                FROM
                    webapp_designation
                    JOIN webapp_employeemodules ON webapp_employeemodules.designation_id = webapp_designation.id
                    JOIN webapp_employeemodules_module ON webapp_employeemodules_module.employeemodules_id = webapp_employeemodules.id
                    JOIN webapp_employeemodules_platform ON webapp_employeemodules_platform.employeemodules_id = webapp_employeemodules_module.employeemodules_id
                    JOIN webapp_platform ON webapp_platform.id = webapp_employeemodules_platform.platform_id
                    JOIN webapp_modules ON webapp_modules.id = webapp_employeemodules_module.modules_id
                ORDER BY EmployeeDesignation, Platform'''
    train_data_df = pd.read_sql_query(query,connection)
    Platforms_df = {}
    platforms = train_data_df.Platform.unique().tolist()
    for platform in platforms:
        platform_df = train_data_df[train_data_df['Platform']== platform]
        Platforms_df[platform] = platform_df

    encoded_Platforms_df = {}
    for platform, platform_df in Platforms_df.items():
        encoded_Platforms_df[platform] = pd.get_dummies(platform_df,columns=['Module'], prefix="",prefix_sep="")
    feature_inputs = {}
    for platform, encoded_df in encoded_Platforms_df.items():
        feature_inputs[platform] = Platforms_df[platform].Module.unique().tolist()
    X = {}
    for platform, feature in feature_inputs.items():
        X[platform] = encoded_Platforms_df[platform][feature_inputs[platform]]
    y = {}
    for platform, feature in feature_inputs.items():
        y[platform] = encoded_Platforms_df[platform].EmployeeDesignation

    data_train = {}
    label_train = {}
    for platform, feature in X.items():
        data_train[platform] = X[platform]
        
    for platform, labels in y.items():
        label_train[platform] = y[platform]

    # # save decision tree model
    # for platform in feature_inputs.keys():
    #     dt = DecisionTreeClassifier()
    #     dt.fit(data_train[platform], label_train[platform])
    #     dt.feature_names = feature_inputs[platform]
    #     model_name = platform + '.sav'
    #     path = os.path.join(settings.BASE_DIR, 'models/dts', model_name)
    #     pickle.dump(dt, open(path, 'wb'))

    # # Save Support Vector Model
    # for platform in feature_inputs.keys():
    #     svc = SVC(gamma='auto',probability=True)
    #     svc.fit(data_train[platform], label_train[platform])
    #     svc.feature_names = feature_inputs[platform]
    #     model_name = platform + '.sav'
    #     path = os.path.join(settings.BASE_DIR, 'models/svcs', model_name)
    #     pickle.dump(svc, open(path, 'wb'))

    # Save Random Forest Model
    for platform in feature_inputs.keys():
        rfc = RandomForestClassifier(n_estimators=100)
        rfc.fit(data_train[platform], label_train[platform])
        rfc.feature_names = feature_inputs[platform]
        model_name = platform + '.sav'
        path = os.path.join(settings.BASE_DIR, 'models/rfcs', model_name)
        pickle.dump(rfc, open(path, 'wb'))
