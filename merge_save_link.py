import pikepdf

def merge_pdfs_with_links(pdf_list, output_path):
    """
    合并多个 PDF 文件并保留目录和链接。
    :param pdf_list: 包含待合并的 PDF 文件路径的列表。
    :param output_path: 合并后的输出文件路径。
    """
    try:
        merged_pdf = pikepdf.Pdf.new()
        for pdf in pdf_list:
            with pikepdf.Pdf.open(pdf) as src_pdf:
                merged_pdf.pages.extend(src_pdf.pages)  # 保留所有的页面及其属性
        merged_pdf.save(output_path)
        print(f"PDF 合并完成，保存至：{output_path}")
    except Exception as e:
        print(f"合并过程中发生错误：{e}")

# 示例用法
pdf_files = ["1.pdf", "2.pdf"]  # 替换为你的 PDF 文件路径
output_file = "merged_output.pdf"       # 输出文件路径
merge_pdfs_with_links(pdf_files, output_file)
