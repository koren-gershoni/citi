import camelot
import pandas as pd

from config.config import Config
from loaders.base import BaseLoader


class CitiEarningsPdfLoader(BaseLoader):
    def __init__(self, config: Config):
        super().__init__(config)

    def load(self) -> pd.DataFrame:
        # tables = camelot.read_pdf(str(path), pages="2", flavor="stream")
        tables = camelot.read_pdf(str(self.config.data.filepath), **self.config.data.pdf.dict())
        df = tables[0].df
        df.columns = df.iloc[2]
        df = df[4:]
        df = df.set_index(df.columns[0])
        df.index = df.index.str.replace(r"\(\d+\)|-", "", regex=True).str.strip()
        return df
