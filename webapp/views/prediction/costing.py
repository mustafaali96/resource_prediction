import pandas as pd
import os
from django.db import connection

def ProjectCost(designation_group, Region):
    project_time = 0
    total_project_cost = 0
    for platform, group in designation_group.items():
        group_hours = {}
        for designation, modules in group.items():
            designation_time = 0
            for module in modules:
                query = '''SELECT
                                webapp_modules.module AS module,
                                webapp_modules.time AS module_time
                            FROM 
                                webapp_modules
                            WHERE module = :module'''
                module_time_df = pd.read_sql_query(query, connection, params={'module': module})
                platform_designation_time = module_time_df['module_time'].values
                designation_time += platform_designation_time[0]
            project_time += designation_time
            group_hours[designation] = designation_time
        designation_group[platform]['Time'] = group_hours
        
    for platform, stack in designation_group.items():
        # print("\n\t****", platform, "****\n")
        designation_time = stack["Time"]
        platform_cost = 0
        platform_time = 0
        designation_rate = {}
        for designation, time in designation_time.items():
            query = '''SELECT
                            webapp_designation.designation AS Designation,
                            webapp_region.name AS Region,
                            webapp_userhourlyrate.rate AS User_rate
                        FROM
                            webapp_designation 
                            JOIN webapp_userhourlyrate ON webapp_userhourlyrate.designation_id = webapp_designation.id
                            JOIN webapp_region ON webapp_region.id = webapp_userhourlyrate.region_id
                        WHERE Designation = :designation AND Region = :region;'''
            user_rate = pd.read_sql_query(query, connection, params={'designation': designation, 'region':Region})
            rate = user_rate.User_rate.values[0] * time
            # print(designation,"required",designation_time[designation], "hrs and cost will be:", rate, "$")
            platform_cost += int(rate)
            platform_time += time
            designation_rate[designation] = rate
        designation_group[platform]["Designation Cost"] = designation_rate
        total_project_cost += platform_cost
        # print("\nTotal time required for",platform, "is", platform_time)
        # print("Total cost for",platform, "is", platform_cost)
        designation_group[platform]['Platform Cost'] = platform_cost

    designation_group["Total Project Time"] = project_time
    designation_group["Total Project Cost"] = total_project_cost
    # print("\nTotal Project Cost is:",total_project_cost)

    return designation_group