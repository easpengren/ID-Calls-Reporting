#!/usr/bin/python
import geopandas
import numpy as np
import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt
import descartes
import contextily as ctx
import civis
from matplotlib.backends.backend_pdf import PdfPages

from questions import QUESTIONS_ANSWERS_LOOKUP
questions = QUESTIONS_ANSWERS_LOOKUP
questions_df = pd.DataFrame.from_dict(questions)
questions_df.columns=['question_name', 'question']

from mpl_toolkits.axes_grid1 import make_axes_locatable
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

with PdfPages('multipage_pdf.pdf') as pdf:
    for ind in questions_df.index:
        question_name = questions_df['question_name'][ind]
        if question_name != 'intro':
            sql = "select cd, " + question_name +", count("+ question_name + ") from collectivepac.id_calls_match where cd is not null group by cd, " + question_name + " order by cd"
            df = civis.io.read_civis_sql(sql, "TMC", use_pandas=True)
            df['cd'] = df['cd'].astype(int)






            table = pd.pivot_table(df, index='cd', values='count', columns=[question_name],
                      aggfunc=np.sum)
            print(table)


            from sqlalchemy import create_engine
            db_connection_url = "postgres://postgres:postgrespassword@10.0.0.3:5432/postgres";
            engine = create_engine(db_connection_url)
            state_cd_file=geopandas.read_postgis("select * from tl_2019_us_cd116 where statefp = '13'", engine, geom_col = 'geom')
            state_cd_file = state_cd_file.rename(columns={"cd116fp": "cd"})
            state_cd_file = state_cd_file.to_crs(epsg=3857)
            state_cd_file['cd'] = state_cd_file['cd'].astype(int)
            state_cd_file = state_cd_file.merge(table, how='left', on='cd')
            state_cd_file = state_cd_file.fillna(0)
            print(state_cd_file)
            print(state_cd_file.columns)
            columns = state_cd_file.columns.tolist()
            for column in columns[14:]:
                print(column)
                fig, ax = plt.subplots(1, 1)

                divider = make_axes_locatable(ax)


                fig.set_size_inches([7, 10])

                state_cd_file.plot(column,
                    ax=ax,
                    cmap='OrRd',
                    legend=True,
                    legend_kwds={'label': column,'orientation': "horizontal"},
                    alpha = 0.7,
                    edgecolor = "black"



                )
                ctx.add_basemap(ax)
                ax.set_axis_off()
                plt.axis('off')
                plt.title(question_name, loc='center')
                pdf.savefig()
                plt.show()
                plt.close()
