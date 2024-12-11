import logging
from typing import Literal

from omegaconf import OmegaConf, DictConfig
from pydantic import BaseModel, Field
from dotenv import load_dotenv

def setup_logging():
    """Configure basic logging for the application."""
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )


class XlsxConfig(BaseModel):
    sheet_name: str | None = Field(default=None)
    header: list[int] | None = Field(default=None)
    skiprows: int | None = Field(default=None)


class PdfConfig(BaseModel):
    flavor: str
    pages: str | None = Field(default=None)


class DataConfig(BaseModel):
    filepath: str
    xlsx: XlsxConfig = Field(default_factory=lambda: XlsxConfig)
    pdf: PdfConfig = Field(default_factory=lambda: PdfConfig)
    values_to_extract: list[str] | dict[str, str]


class LLMConfig(BaseModel):
    name: str = Field(default="bartowski/Mistral-Nemo-Instruct-2407-GGUF")


class Config(BaseModel):
    mode: Literal["llm", "non-llm"] = Field(default="non-llm")
    data: DataConfig = Field(default_factory=DataConfig)
    llm: LLMConfig = Field(default_factory=LLMConfig)

    @classmethod
    def from_omegaconf(cls, conf: DictConfig) -> "Config":
        conf_dict = OmegaConf.to_container(conf, resolve=True)
        return cls.parse_obj(conf_dict)


def get_config(yaml_path: str | None = None) -> Config:
    load_dotenv()
    if yaml_path:
        conf = OmegaConf.load(yaml_path)
        config = Config.from_omegaconf(conf)
    else:
        config = Config()
    setup_logging()
    return config
