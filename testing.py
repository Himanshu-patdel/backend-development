# from PIL  import Image, ImageChops
# import io
# import fitz 
# from pdflatex import PDFLaTeX

# def trim_white_space(img_buffer: io.BytesIO, padding: int = 50) -> io.BytesIO:
#     with Image.open(img_buffer) as img:
#         img = img.convert("RGB")

#         bg_color = (255, 255, 255)
#         bg = Image.new("RGB", img.size, bg_color)
#         diff = ImageChops.difference(img, bg)
#         bbox = diff.getbbox()

#         if bbox:
#             # Adding padding
#             left = max(0, bbox[0] - padding)
#             upper = max(0, bbox[1] - padding)
#             right = min(img.size[0], bbox[2] + padding)
#             lower = min(img.size[1], bbox[3] + padding)

#             # Crop the image with the adjusted bounding box
#             trimmed_img = img.crop((left, upper, right, lower))
#             output_buffer = io.BytesIO()
#             trimmed_img.save(output_buffer, format="PNG")
#             output_buffer.seek(0)
#             return output_buffer

#     return img_buffer

# def convert_latex_to_png_images(latex_code: str):
   
#         # Convert LaTeX code to PDF
#         binary_string = latex_code.encode('utf-8')
#         pdfl = PDFLaTeX.from_binarystring(binary_string, jobname="latex_document")
#         pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=False, keep_log_file=False)
        
#         # Open the PDF document
#         pdf_buffer = io.BytesIO(pdf)
#         pdf_document = fitz.open("pdf", pdf_buffer)
        
#         # Process each page and convert to PNG
#         png_image_urls = []
#         for page_number in range(len(pdf_document)):
#             page = pdf_document.load_page(page_number)
#             pixmap = page.get_pixmap(dpi=300)
            
#             # Convert Pixmap to in-memory image buffer
#             img_buffer = io.BytesIO(pixmap.tobytes("png"))
            
#              # Trim whitespace and add padding
#             trimmed_img_buffer = trim_white_space(img_buffer)
        
    
# convert_latex_to_png_images()


# from PIL import Image, ImageChops
# import io
# import fitz
# from pdflatex import PDFLaTeX

# def trim_white_space(img_buffer: io.BytesIO, padding: int = 50) -> io.BytesIO:
#     with Image.open(img_buffer) as img:
#         img = img.convert("RGB")

#         bg_color = (255, 255, 255)
#         bg = Image.new("RGB", img.size, bg_color)
#         diff = ImageChops.difference(img, bg)
#         bbox = diff.getbbox()

#         if bbox:
#             # Adding padding
#             left = max(0, bbox[0] - padding)
#             upper = max(0, bbox[1] - padding)
#             right = min(img.size[0], bbox[2] + padding)
#             lower = min(img.size[1], bbox[3] + padding)

#             # Crop the image with the adjusted bounding box
#             trimmed_img = img.crop((left, upper, right, lower))
#             output_buffer = io.BytesIO()
#             trimmed_img.save(output_buffer, format="PNG")
#             output_buffer.seek(0)
#             return output_buffer

#     return img_buffer

# def convert_latex_to_png_images(latex_code: str, output_dir: str = "output_images_latex"):
#     # Convert LaTeX code to PDF
#     binary_string = latex_code.encode('utf-8')
#     pdfl = PDFLaTeX.from_binarystring(binary_string, jobname="latex_document")
#     pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=False, keep_log_file=False)

#     # Open the PDF document
#     pdf_buffer = io.BytesIO(pdf)
#     pdf_document = fitz.open("pdf", pdf_buffer)

#     # Process each page and convert to PNG
#     for page_number in range(len(pdf_document)):
#         page = pdf_document.load_page(page_number)
#         pixmap = page.get_pixmap(dpi=300)

#         # Convert Pixmap to in-memory image buffer
#         img_buffer = io.BytesIO(pixmap.tobytes("png"))

#         # Trim whitespace and add padding
#         trimmed_img_buffer = trim_white_space(img_buffer)

#         # Save the PNG image
#         trimmed_img = Image.open(trimmed_img_buffer)
#         output_file = f"{output_dir}/page_{page_number + 1}.png"
#         trimmed_img.save(output_file, format="PNG")
#         print(f"Saved: {output_file}")

# # Example usage
# latex_code = r"""
# \documentclass{article}
# \begin{document}
# Hello, world!
# \end{document}
# """
# convert_latex_to_png_images(latex_code)


# from PIL import Image, ImageChops
# import io
# import fitz
# import os
# from pdflatex import PDFLaTeX

# def trim_white_space(img_buffer: io.BytesIO, padding: int = 50) -> io.BytesIO:
#     with Image.open(img_buffer) as img:
#         img = img.convert("RGB")

#         bg_color = (255, 255, 255)
#         bg = Image.new("RGB", img.size, bg_color)
#         diff = ImageChops.difference(img, bg)
#         bbox = diff.getbbox()

#         if bbox:
#             # Adding padding
#             left = max(0, bbox[0] - padding)
#             upper = max(0, bbox[1] - padding)
#             right = min(img.size[0], bbox[2] + padding)
#             lower = min(img.size[1], bbox[3] + padding)

#             # Crop the image with the adjusted bounding box
#             trimmed_img = img.crop((left, upper, right, lower))
#             output_buffer = io.BytesIO()
#             trimmed_img.save(output_buffer, format="PNG")
#             output_buffer.seek(0)
#             return output_buffer

#     return img_buffer

# def convert_latex_to_png_images(latex_code: str, output_dir: str = "output_images"):
#     # Ensure the output directory exists
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)
    
#     # Convert LaTeX code to PDF
#     binary_string = latex_code.encode('utf-8')
#     pdfl = PDFLaTeX.from_binarystring(binary_string, jobname="latex_document")
#     pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=False, keep_log_file=False)

#     # Open the PDF document
#     pdf_buffer = io.BytesIO(pdf)
#     pdf_document = fitz.open("pdf", pdf_buffer)

#     # Process each page and convert to PNG
#     for page_number in range(len(pdf_document)):
#         page = pdf_document.load_page(page_number)
#         pixmap = page.get_pixmap(dpi=300)

#         # Convert Pixmap to in-memory image buffer
#         img_buffer = io.BytesIO(pixmap.tobytes("png"))

#         # Trim whitespace and add padding
#         trimmed_img_buffer = trim_white_space(img_buffer)

#         # Save the PNG image
#         trimmed_img = Image.open(trimmed_img_buffer)
#         output_file = os.path.join(output_dir, f"page_{page_number + 1}.png")
#         trimmed_img.save(output_file, format="PNG")
#         print(f"Saved: {output_file}")

# # Example usage
# latex_code = r"""
# \documentclass{article}
# \begin{document}
# Hello, world!
# \end{document}
# """
# convert_latex_to_png_images(latex_code)

import uuid
from PIL import Image, ImageChops
import io
import fitz
import os
from pdflatex import PDFLaTeX

def trim_white_space(img_buffer: io.BytesIO, padding: int = 10) -> io.BytesIO:
    with Image.open(img_buffer) as img:
        img = img.convert("RGB")

        bg_color = (255, 255, 255)
        bg = Image.new("RGB", img.size, bg_color)
        diff = ImageChops.difference(img, bg)
        bbox = diff.getbbox()

        # Debug: Save original and diff images
        img.save("original_image.png")
        diff.save("diff_image.png")

        if bbox:
            # Adding padding
            left = max(0, bbox[0] - padding)
            upper = max(0, bbox[1] - padding)
            right = min(img.size[0], bbox[2] + padding)
            lower = min(img.size[1], bbox[3] + padding)

            # Crop the image with the adjusted bounding box
            trimmed_img = img.crop((left, upper, right, lower))
            
            # Debug: Save trimmed image
            trimmed_img.save("trimmed_image.png")
            
            output_buffer = io.BytesIO()
            trimmed_img.save(output_buffer, format="PNG")
            output_buffer.seek(0)
            return output_buffer

    return img_buffer

def convert_latex_to_png_images(latex_code: str):
    # Convert LaTeX code to PDF
    binary_string = latex_code.encode('utf-8')
    pdfl = PDFLaTeX.from_binarystring(binary_string, jobname="latex_document")
    pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=False, keep_log_file=False)

    # Open the PDF document
    pdf_buffer = io.BytesIO(pdf)
    pdf_document = fitz.open("pdf", pdf_buffer)

    # Process each page and convert to PNG
    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        pixmap = page.get_pixmap(dpi=300)

        # Convert Pixmap to in-memory image buffer
        img_buffer = io.BytesIO(pixmap.tobytes("png"))

        # Trim whitespace and add padding
        trimmed_img_buffer = trim_white_space(img_buffer)

        # Save the PNG image
        image_filename = f"temp_{uuid.uuid4().hex[:5]}.png"
        trimmed_img = Image.open(trimmed_img_buffer)
        trimmed_img.save(image_filename, format="PNG")
        print(f"Saved: {image_filename}")

# Example usage
# latex_code = r"""
# \documentclass{article}
# \begin{document}
# Hello, world!
# \end{document}
# """
# latex_code=r""" \\documentclass{article}\n\\usepackage{tcolorbox}\n\\usepackage{caption}\n\\usepackage{tikz}\n\\usepackage[utf8]{inputenc}\n\n% Adjust caption settings\n\\captionsetup[figure]{labelformat=empty, labelsep=none}\n\n% Define a new command for the subcomponent box\n\\newcommand{\\coloredBoxWithArc}[2]{\n    \\begin{tikzpicture}\n        \\node (box) [inner sep=0pt] {\n            \\begin{tcolorbox}[colframe=black, colback=white, sharp corners, boxrule=0.5mm, left=2mm, right=2mm, top=1mm, bottom=1mm, boxsep=10pt]\n                
#  {#1}\n            \\end{tcolorbox}\n        };\n        \\draw[ thick,-] (box.north east) arc(150:80:1.5cm) node[pos=1.3] {#2};\n    \\end{tikzpicture}\n}\n\n\\begin{document}\n\\pagenumbering{gobble}\n\n\\begin{figure}\n    \\vspace*{-3cm}\n    \\begin{tikzpicture}\n    \\node (box) [inner sep=0pt] {\n        \\begin{tcolorbox}[colframe=black, colback=white, sharp corners, boxrule=0.5mm]\n            Dynamic updating system\n        \n            % Use the new command to create subcomponent boxes\n            \\coloredBoxWithArc{Search engine database}{301}\n            \n        \\end{tcolorbox}\n    };\n    \\draw[ thick,-] (box.north east) arc(150:80:1.5cm) node[pos=1.3] {300};\n    \\end{tikzpicture}\n    \n\\caption {\\textbf{Fig. 3}}\n    \n\\end{figure}\n\n\\end{document}
# """
latex_code='''

\\documentclass{article}\n\\usepackage{tcolorbox}\n\\usepackage{caption}\n\\usepackage{tikz}\n\\usepackage[utf8]{inputenc}\n\n% Adjust caption settings\n\\captionsetup[figure]{labelformat=empty, labelsep=none}\n\n% Define a new command for the subcomponent box\n\\newcommand{\\coloredBoxWithArc}[2]{\n    \\begin{tikzpicture}\n        \\node (box) [inner sep=0pt] {\n            \\begin{tcolorbox}[colframe=black, colback=white, sharp corners, boxrule=0.5mm, left=2mm, right=2mm, top=1mm, bottom=1mm, boxsep=10pt]\n           
{#1}\n            \\end{tcolorbox}\n        };\n        \\draw[ thick,-] (box.north east) arc(150:80:1.5cm) node[pos=1.3] {#2};\n  
\\end{tikzpicture}\n}\n\n\\begin{document}\n\\pagenumbering{gobble}\n\n\\begin{figure}\n    \\vspace*{-3cm}\n    \\begin{tikzpicture}\n    \\node (box) [inner sep=0pt] {\n        \\begin{tcolorbox}[colframe=black, colback=white, sharp corners, boxrule=0.5mm]\n            Dynamic updating system\n        \n            % Use the new command to create subcomponent boxes\n            \\coloredBoxWithArc{Search engine database}{301}\n            \n        \\end{tcolorbox}\n    };\n    \\draw[ thick,-] (box.north east) arc(150:80:1.5cm) node[pos=1.3] {300};\n    \\end{tikzpicture}\n    \n\\caption {\\textbf{Fig. 3}}\n    \n\\end{figure}\n\n\\end{document}


'''
convert_latex_to_png_images(latex_code)
