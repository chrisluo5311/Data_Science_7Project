import pandas as pd
import sqlite3

filen_names = ["ddf--datapoints--gdp_pcap--by--country--time", 
               "ddf--datapoints--lex--by--country--time",
               "ddf--datapoints--pop--by--country--time",
               "ddf--entities--geo--country"]

table_names = ["gdp_per_capita", "life_expectancy", "population", "geography"]

def load_data(file_names, table_names) -> dict[str, pd.DataFrame]:
    df_dict = dict()
    for file_name, table_name in zip(file_names, table_names):
        df = pd.read_csv(f"./gapminder_clone/data/{file_name}.csv")
        df_dict[table_name] = df
    return df_dict



def create_sqlite_db(df_dict) -> None:
    connection = sqlite3.connect("./gapminder_clone/data/gapminder.db")
    for k, v in df_dict.items():
        v.to_sql(k, connection, if_exists="replace", index=False)
    connection.close()


if __name__ == "__main__":
    df_dict = load_data(filen_names, table_names)
    # print(df_dict)
    create_sqlite_db(df_dict)