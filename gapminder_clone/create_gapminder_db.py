import pandas as pd
import sqlite3

class CreateGapminderDb:
    def __init__(self):
        self.filen_names = ["ddf--datapoints--gdp_pcap--by--country--time", 
                            "ddf--datapoints--lex--by--country--time",
                            "ddf--datapoints--pop--by--country--time",
                            "ddf--entities--geo--country"]

        self.table_names = ["gdp_per_capita", "life_expectancy", 
                            "population", "geography"]

    def import_as_dataframe (self) -> dict[str, pd.DataFrame]:
        df_dict = dict()
        for file_name, table_name in zip(self.filen_names, self.table_names):
            df = pd.read_csv(f"./gapminder_clone/data/{file_name}.csv")
            df_dict[table_name] = df
        return df_dict

    def create_database(self) -> None:
        connection = sqlite3.connect("./gapminder_clone/data/gapminder.db")
        df_dict = self.import_as_dataframe()
        for k, v in df_dict.items():
            v.to_sql(k, connection, if_exists="replace", index=False)
        drop_view_if_exists = """
        DROP VIEW IF EXISTS plotting;
        """ 
        create_view_if_exists = """
        CREATE VIEW plotting AS
        SELECT geography.name AS country_name,
               gdp_per_capita.time AS dt_year,
               gdp_per_capita.gdp_pcap AS gdp_per_capita,
               geography.world_4region AS continent,
               life_expectancy.lex AS life_expectancy,
               population.pop AS population
          FROM gdp_per_capita
          JOIN geography
            ON gdp_per_capita.country = geography.country
          JOIN life_expectancy
            ON gdp_per_capita.country = life_expectancy.country AND
               gdp_per_capita.time = life_expectancy.time
          JOIN population
            ON gdp_per_capita.country = population.country AND
               gdp_per_capita.time = population.time
         WHERE gdp_per_capita.time < 2026;
        """
        cursor = connection.cursor()
        cursor.execute(drop_view_if_exists)
        cursor.execute(create_view_if_exists)
        connection.close()

if __name__ == "__main__":
    create_gapminder_db = CreateGapminderDb()
    create_gapminder_db.create_database()
