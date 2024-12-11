from abc import ABC

import pandas as pd

from config.config import Config


class BaseLoader(ABC):
    def __init__(self, config: Config):
        self.config = config

    @staticmethod
    def load() -> pd.DataFrame:
        raise NotImplementedError("load function not implemented")


class LoaderManager:
    pass
