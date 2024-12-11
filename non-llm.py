import csv
from pipelines import pdf_pipeline, xlsx_pipeline

if __name__ == "__main__":
    df_pdf = pdf_pipeline.run()
    df_excel = xlsx_pipeline.run()
    df_excel = df_excel.iloc[[i for i in range(len(df_excel)) if i != 2]]
    header = ["Metric Name", "Value from PDF (Q3 and Q2)", "Value from Excel (Q3 and Q2)", "Match/No Match"]
    metrics = ["Revenues", "Net Income", "Book value per share", "Tangible book value per share", "CET1 Capital Ratio"]
    with open("results/non_llm_based.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for index, ((row_excel_index, row_excel), (_, row_pdf)) in enumerate(zip(df_excel.iterrows(), df_pdf.iterrows())):
            pdf_str = f"{row_pdf.iloc[0]}/{row_pdf.iloc[1]}"
            excel_str = f"{row_excel.iloc[1]}/{row_excel.iloc[0]}"
            writer.writerow([
                metrics[index],
                pdf_str,
                excel_str,
                "Match" if pdf_str == excel_str else "No Match"
            ])
