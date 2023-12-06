from PySide6.QtCore import QUrl
from PySide6.QtPrintSupport import QPrintDialog, QPrinter
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

class BillViewer(QMainWindow):
    def __init__(self, pdf_path):
        super().__init__()
        self.pdf_path = pdf_path
        self.setWindowTitle("Bill Viewer")

        self.printer = QPrinter()

        self.web_view = QWebEngineView()
        self.web_view.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.web_view.settings().setAttribute(QWebEngineSettings.PdfViewerEnabled, True)
        self.web_view.load(QUrl.fromLocalFile(pdf_path))

        # self.print_button = QPushButton("Print Bill")
        # self.print_button.clicked.connect(self.print_bill)

        layout = QVBoxLayout()
        layout.addWidget(self.web_view)
        # layout.addWidget(self.print_button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    # def print_bill(self):
    #     print_dialog = QPrintDialog(self)
    #     if print_dialog.exec_() == QPrintDialog.Accepted:
    #         self.web_view.print(print_dialog.printer())
    #
    # def print_done(self, success):
    #     if success:
    #         print("Printing completed successfully.")
    #     else:
    #         print("Printing failed.")


def generate_bill(cart_items, store_name="LocalStore", store_address="123 Main St", gst_no="GST123"):
    try:
        pdf_filename = "bill.pdf"

        # Create a PDF document
        doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
        elements = []

        # Store information
        store_info = [
            [f"{store_name}\n{store_address}\nGST No: {gst_no}"]
        ]
        store_table = Table(store_info, colWidths=[540])
        elements.append(store_table)

        # Bill summary
        bill_summary = [
            ["Bill Summary:"],
            [f"Grand Total: {calculate_grand_total(cart_items)}"]  # Replace with your actual total amount field
        ]
        bill_table = Table(bill_summary, colWidths=[540])
        elements.append(bill_table)

        # Items purchased section
        items_data = [["","Items Purchased",""]]
        headers = list(cart_items[0].keys())
        headerstoshow = ['No', 'Product', 'HSN', 'Price', 'Qty', 'Discount', 'Amount', 'CGST', 'SGST', 'IGST', 'T.Tax', 'G.Total']

        items_data.append(headerstoshow)
        for item in cart_items:
            items_data.append([item[key] for key in headers])
        items_table = Table(items_data, colWidths=[45] * len(headers))
        items_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, 1), colors.beige),
        ]))
        elements.append(items_table)

        # Build the PDF document
        doc.build(elements)

        print(f"PDF generated successfully: {pdf_filename}")
        return pdf_filename

    except Exception as e:
        print(f"Error generating PDF: {e}")

def calculate_grand_total(cart_items):
    total = sum(float(item['Grand Total']) for item in cart_items)
    return round(total, 2)


