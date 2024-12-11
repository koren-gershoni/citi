from config.config import get_config, Config
from loaders.xlsx import XlsxLoader
from processors.xlsx import CitiEarningsXlsxProcessor


def run():
    config: Config = get_config("config/xlsx.yaml")
    df = XlsxLoader(config).load()
    df = CitiEarningsXlsxProcessor().process(df)
    df = df.loc[config.data.values_to_extract]
    return df


if __name__ == "__main__":
    run()
