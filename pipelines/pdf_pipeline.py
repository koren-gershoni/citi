from config.config import get_config, Config
from loaders.pdf import CitiEarningsPdfLoader
from loaders.xlsx import XlsxLoader
from processors.xlsx import CitiEarningsXlsxProcessor


def run():
    config: Config = get_config("config/pdf.yaml")
    df = CitiEarningsPdfLoader(config).load()
    df = df.loc[config.data.values_to_extract.keys()]
    df = df.rename(index=config.data.values_to_extract)
    return df


if __name__ == "__main__":
    run()
