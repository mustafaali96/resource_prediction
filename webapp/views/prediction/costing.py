import pandas as pd
import os
from django.db import connection
import math


def ProjectCost(designation_group, project_req_time, Region):
    data = {}
    project_time = 0
    total_project_cost = 0
    for platform, group in designation_group.items():
        platform_time = 0
        data[platform] = {}
        for designation, modules in group.items():
            # data[platform][designation] = {}
            data[platform][designation] = []
            designation_time = 0
            for module in modules:
                module_data = {}
                # data[platform][designation][module] = {}
                query = '''SELECT
                                webapp_modules.module AS module,
                                webapp_modules.time AS module_time
                            FROM 
                                webapp_modules
                            WHERE module = :module'''
                module_time_df = pd.read_sql_query(query, connection, params={'module': module})
                module_time = module_time_df['module_time'].values
                # data[platform][designation][module]["Module Time"] = module_time[0]
                module_data['Module Name'] = module
                module_data['Module Time'] = module_time[0]
                module_data['Module Cost'] = 0
                data[platform][designation].append(module_data)
                designation_time += module_time[0]
            # data[platform][designation]['Developer Time'] = designation_time
            # data[platform][designation]['Developer Cost'] = 0
            developer_data = {}
            no_resources = 1
            temp_designation_time = designation_time
            while designation_time > int(project_req_time):
                no_resources += 1
                designation_time = math.ceil(temp_designation_time/no_resources)
            developer_data['Developer Time'] = designation_time
            developer_data['Developer Cost'] = 0
            developer_data['No of Resources'] = no_resources
            data[platform][designation].append(developer_data)
            platform_time += designation_time

            project_time += designation_time
        data[platform]["Platform Time"] = platform_time
        data[platform]["Platform Cost"] = 0
        
    # for platform, stack in designation_group.items():
    #     # print("\n\t****", platform, "****\n")
    #     designation_time = stack["Time"]
    #     platform_cost = 0
    #     platform_time = 0
    #     designation_rate = {}
    #     for designation, time in designation_time.items():
    #         query = '''SELECT
    #                         webapp_designation.designation AS Designation,
    #                         webapp_region.name AS Region,
    #                         webapp_userhourlyrate.rate AS User_rate
    #                     FROM
    #                         webapp_designation 
    #                         JOIN webapp_userhourlyrate ON webapp_userhourlyrate.designation_id = webapp_designation.id
    #                         JOIN webapp_region ON webapp_region.id = webapp_userhourlyrate.region_id
    #                     WHERE Designation = :designation AND Region = :region;'''
    #         user_rate = pd.read_sql_query(query, connection, params={'designation': designation, 'region':Region})
    #         rate = user_rate.User_rate.values[0] * time
    #         # print(designation,"required",designation_time[designation], "hrs and cost will be:", rate, "$")
    #         platform_cost += int(rate)
    #         platform_time += time
    #         designation_rate[designation] = rate
    #     designation_group[platform]["Designation Cost"] = designation_rate
    #     total_project_cost += platform_cost
    #     # print("\nTotal time required for",platform, "is", platform_time)
    #     # print("Total cost for",platform, "is", platform_cost)
    #     designation_group[platform]['Platform Cost'] = platform_cost


    # Each module time and cost
    for platform, designations_module_time in data.items():
        platform_cost = 0
        for designation, modules_data in designations_module_time.items():
            if designation == 'Platform Time' or designation == 'Platform Cost':
                pass
            else:
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
                for module_data in modules_data:
                    for module, info in module_data.items():
                        if(module == 'Developer Time'):
                            cost = info * user_rate.User_rate.values[0] * module_data['No of Resources']
                            module_data['Developer Cost'] = cost
                            platform_cost += cost
                        elif(module == 'Module Time'):
                            cost = info * user_rate.User_rate.values[0]
                            module_data['Module Cost'] = cost

                # for modules, designation_time in module_time.items():
                #     if(modules == 'Developer Time' or modules == 'Developer Cost'):
                #         cost = module_time['Developer Time'] * user_rate.User_rate.values[0]
                #         data[platform][designation]['Developer Cost'] = cost
                #         platform_cost += cost
                #     else:
                #         cost = designation_time['Module Time'] * user_rate.User_rate.values[0]
                        # data[platform][designation][modules]['Module Cost'] = cost
        data[platform]["Platform Cost"] = platform_cost
        total_project_cost += platform_cost
    data["Total Project Time"] = project_time
    data["Total Project Cost"] = total_project_cost
    return data