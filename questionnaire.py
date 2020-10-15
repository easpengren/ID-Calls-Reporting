#!/usr/bin/env python3
import sys
import pandas as pd
import matplotlib.pyplot as plt
import textwrap
import sys
import civis
from tabulate import tabulate
from matplotlib.backends.backend_pdf import PdfPages



output_file = "GA_Questionnaire"

def pprint_df(dframe) -> object:
    print(tabulate(dframe, headers='keys', tablefmt="plain", showindex=False), file=text_file)

from questions import QUESTIONS_ANSWERS_LOOKUP
questions = QUESTIONS_ANSWERS_LOOKUP
questions_df = pd.DataFrame.from_dict(questions)
questions_df.columns=['question_name', 'question']

call_data_df = pd.read_csv('GA_Calls.csv')
call_data_df = call_data_df[call_data_df.state == 'GA']
call_data_df = call_data_df.rename(columns = {'state' : 'State', 'cd':'CD'})
print(call_data_df)

with open(output_file + '.txt', "w") as text_file:

    for row in questions_df.index:
        question_name = questions_df['question_name'][row]
        question = questions_df['question'][row]
        with pd.option_context('display.max_rows', 1000, 'display.max_columns', 1000, 'display.width', 80):
            question_header = question_name+': '+question
            print(textwrap.fill(question_header, width=80), file=text_file)
            print('\n', file=text_file)
            if question_name != 'intro':
                #call_data_pivot = call_data_df.pivot_table('ncvanid', index=('city','gender'), columns=[question_name], aggfunc='count')
                #print(tabulate(call_data_pivot, headers='keys', tablefmt='psql'))

                call_data_cross = pd.crosstab(index=[call_data_df['CD'], call_data_df[question_name]], columns=call_data_df['State'])
                pd.options.display.float_format = '{:.0f}'.format
                print(call_data_cross, file=text_file)
                print('\n', file=text_file)




