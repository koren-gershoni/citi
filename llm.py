import csv

from langchain_community.document_loaders import PyMuPDFLoader, UnstructuredExcelLoader
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()


class CitiEarningReview(BaseModel):
    q3_revenues: int = Field(description="Total revenues, net of interest expense in Q3 2024")
    q2_revenues: int = Field(description="Total revenues, net of interest expense in Q2 2024")
    q3_net_income: int = Field(description="Net income attributable to non-controlling interest in Q3 2024")
    q2_net_income: int = Field(description="Net income attributable to non-controlling interest in Q2 2024")
    q3_book_value_per_share: float = Field(description="Book value per share in Q3 2024")
    q2_book_value_per_share: float = Field(description="Book value per share in Q2 2024")
    q3_tangible_book_value_per_share: float = Field(description="Tangible book value per share in Q3 2024")
    q2_tangible_book_value_per_share: float = Field(description="Tangible book value per share in Q2 2024")
    q3_cet1_capital_share: float = Field(description="CET1 Capital Ratio Q3 2024")
    q2_cet1_capital_share: float = Field(description="CET1 Capital Ratio Q2 2024")


if __name__ == "__main__":
    model = ChatOpenAI(model="gpt-4o-mini")
    pages_py = PyMuPDFLoader("./data/2024pr-qtr3rslt.pdf").load()
    structured_llm = model.with_structured_output(CitiEarningReview)
    pdf_output = structured_llm.invoke(pages_py[1].page_content)

    elements = UnstructuredExcelLoader("./data/3Q24-SUPP-ForWeb.xlsx", mode="single").load()
    excel_output = structured_llm.invoke(elements[0].page_content)
    print(pdf_output)
    print(excel_output)

    header = ["Metric Name", "Value from PDF (Q3 and Q2)", "Value from Excel (Q3 and Q2)", "Match/No Match"]
    with open("results/llm_based.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)

        writer.writerow([
            "Revenues",
            f"{pdf_output.q3_revenues}/{pdf_output.q2_revenues}",
            f"{excel_output.q3_revenues}/{excel_output.q2_revenues}",
            ""
        ])

        writer.writerow([
            "Net Income",
            f"{pdf_output.q3_net_income}/{pdf_output.q2_net_income}",
            f"{excel_output.q3_net_income}/{excel_output.q2_net_income}",
            ""
        ])
        writer.writerow([
            "Book Value per Share",
            f"{pdf_output.q3_book_value_per_share}/{pdf_output.q2_book_value_per_share}",
            f"{excel_output.q3_book_value_per_share}/{excel_output.q2_book_value_per_share}"
            ""
        ])
        writer.writerow([
            "Tangible Book Value per Share",
            f"{pdf_output.q3_tangible_book_value_per_share}/{pdf_output.q2_tangible_book_value_per_share}",
            f"{excel_output.q3_tangible_book_value_per_share}/{excel_output.q2_tangible_book_value_per_share}"
            ""
        ])
        writer.writerow([
            "CET1 Capital Ratio",
            f"{pdf_output.q3_cet1_capital_share}/{pdf_output.q2_cet1_capital_share}",
            f"{excel_output.q3_cet1_capital_share}/{excel_output.q2_cet1_capital_share}"
            ""
        ])


