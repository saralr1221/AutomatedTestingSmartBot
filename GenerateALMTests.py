#!/usr/bin python
# -*- coding: utf-8 -*-

#srieck 4.08.2025

import pandas as pd
import openpyxl
import GetTestResults2
import main


############### hardcoded stuff ###############

test_steps = {'Step Name (Design Steps)': ["Step 1", "Step 2", "Step 3"], 
    'Description (Design Steps)': [
        "Go to Lorenz Submission Repository at: https://docubridge-cder.test.fda.gov/docubridge/submission-repository",
        "Set the Server to CDER-Test environment (If it is not already set to CDER-Test) Select Windows Authentication option from the Login using drop down (if it is not already selected) and click the Login button.",
        "Select PREPROD_WIN_CDPOOL from the Pool selection"
        ],
    'Expected Result (Design Steps)': [
        "System displays the login screen.",
        "System displays the Submission Repository dashboard screen.",
        "PREPROD_WIN_CDPOOL is selected"
        ]}

df_first_lines = pd.DataFrame(test_steps)

tester = "AutomatedTest"

############### generate ALM tests ###############

def generate_steps():
    df = GetTestResults2.DF
    apps_count = main.i_end
    steps = []
    desc = []
    eresult = []
    for i in range(main.i_start, main.i_end):
        app_num = df['Application'].iloc[i]
        sequence_num = df['Sequence'].iloc[i]
        ex_result = df['Expected Error'].iloc[i]
        steps.append("Step {}".format(i+4))
        desc.append("Find application {} sequence {} and validate it.".format(app_num, sequence_num))
        eresult.append(ex_result)
    df = pd.DataFrame(steps, columns=['Step Name (Design Steps)'])
    df2 = pd.DataFrame(desc, columns=['Description (Design Steps)'])
    df3 = pd.DataFrame(eresult, columns=['Expected Result (Design Steps)'])
    frames = [df, df2, df3]
    new_df = pd.concat(frames, axis=1)
    df4 = pd.DataFrame(new_df)
    return df4, apps_count


def putTogether():
    df4, apps_count = generate_steps()
    last_line = {'Step Name (Design Steps)': ["Step {}".format(apps_count + 4)], 
    'Description (Design Steps)': ["Close submission repository"],
    'Expected Result (Design Steps)': ["Verify that the application was closed"]}
    l = pd.DataFrame(last_line)
    frames1 = [df_first_lines, df4, l]
    n = pd.concat(frames1, axis=0).reset_index(drop=True)
    print(n)
    return n


if __name__ == '__main__':
    df = putTogether()
    df['Exec Date'] = pd.Timestamp.today().strftime('%Y-%m-%d')
    df['Type'] = "MANUAL"
    df['Test Name'] = "TEST Profile 1.6.8.2"
    df['Subject'] = "Profile Testing"
    df['Execution Status'] = "Passed"
    df['Responsible Tester'] = "Sara Rieck"
    print(df)
    df.to_csv(r'C:\Users\Sara.Rieck\ALM_Tests.csv', index=False)
