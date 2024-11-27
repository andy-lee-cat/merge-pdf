# 合并pdf文件
import os
import sys
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()
    try:
        for pdf in pdf_list:
            merger.append(pdf)
        merger.write(output_path)
        print(f"合并完成，输出文件保存至：{output_path}")
    finally:
        merger.close()

if __name__ == '__main__':
    pdf_list = ["1.pdf", "2.pdf", "3.pdf"]
    output = "out.pdf"
    merge_pdfs(pdf_list, output)
