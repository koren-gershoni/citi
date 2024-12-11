from pathlib import Path


import pandas as pd

from config.config import Config
from loaders.base import BaseLoader


class XlsxLoader(BaseLoader):
    def __init__(self, config: Config):
        super().__init__(config)

    def load(self) -> pd.DataFrame:
        df = pd.read_excel(str(self.config.data.filepath), **self.config.data.xlsx.dict())
        return df
