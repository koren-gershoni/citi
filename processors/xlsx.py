import pandas as pd

from processors.base import BaseProcessor


class CitiEarningsXlsxProcessor(BaseProcessor):
    def process(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.dropna(axis=1, how="all")
        first_column = df.columns[0]
        second_column = df.columns[1]

        df.loc[:, first_column] = df[first_column].fillna(df[second_column])
        df.loc[:, second_column] = df[second_column].fillna(df[first_column])
        df = df.drop(second_column, axis=1)

        df.loc[:, first_column] = df[first_column].str.replace(r"\(\d+\)|-", "", regex=True).str.strip()
        df = df.set_index(first_column)
        df = df.dropna(how="all")

        df = df.iloc[:, [3, 4]]
        # rows_to_modify = df.loc["Citigroup's net income (loss)"]
        # df = df.drop(rows_to_modify.iloc[1].name)
        # df.index = df.index.drop_duplicates("Citigroup's net income (loss)")
        return df
