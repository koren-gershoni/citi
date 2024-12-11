from abc import ABC

import pandas as pd


class BaseProcessor(ABC):
    def process(self, df: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError("Process function not implemented")
