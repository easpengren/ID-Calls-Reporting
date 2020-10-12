import civis
import os
import pandas as pd
#CIVIS_API_KEY needs to be grabbed from an environment variable
from tabulate import tabulate
def pprint_df(dframe) -> object:
    print(tabulate(dframe, headers='keys', tablefmt="plain", showindex=False), file=text_file)
output_file = 'report'
from civis_sql import CD_CONTACT_TYPE_QUERY
from civis_sql import CD_PENETRATION_QUERY
from civis_sql import (
    CD_CONTACT_TYPE_QUERY,
    SD_CONTACT_TYPE_QUERY,
    HD_CONTACT_TYPE_QUERY,
    CD_PENETRATION_QUERY,
    SD_PENETRATION_QUERY,
    HD_PENETRATION_QUERY
                       )
with open(output_file+".txt", "w") as text_file:
    sql = CD_CONTACT_TYPE_QUERY
    df = civis.io.read_civis_sql(sql, "TMC", use_pandas=True)
    pprint_df(df)
    print('\n', file=text_file)
    sql = CD_PENETRATION_QUERY
    df = civis.io.read_civis_sql(sql, "TMC", use_pandas=True)
    pprint_df(df)
    print('\n', file=text_file)
    sql = SD_CONTACT_TYPE_QUERY
    df = civis.io.read_civis_sql(sql, "TMC", use_pandas=True)
    pprint_df(df)
    print('\n', file=text_file)
    sql = SD_PENETRATION_QUERY
    df = civis.io.read_civis_sql(sql, "TMC", use_pandas=True)
    print('\n', file=text_file)
    pprint_df(df)
    sql = HD_CONTACT_TYPE_QUERY
    df = civis.io.read_civis_sql(sql, "TMC", use_pandas=True)
    pprint_df(df)
    sql = HD_PENETRATION_QUERY
    df = civis.io.read_civis_sql(sql, "TMC", use_pandas=True)
    pprint_df(df)
    print('\n', file=text_file)