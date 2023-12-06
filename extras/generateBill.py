from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def generate_bill(cart_items, store_name="Your Store", store_address="123 Main St", gst_no="GST123"):
    try:
        pdf_filename = "bill.pdf"

        # Create a PDF document
        doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
        elements = []

        # Store information
        store_info = [
            [f"{store_name}\n{store_address}\nGST No: {gst_no}"]
        ]
        store_table = Table(store_info, colWidths=[400])
        elements.append(store_table)

        # Bill summary
        bill_summary = [
            ["Bill Summary:"],
            [f"Grand Total: {calculate_grand_total(cart_items)}"]  # Replace with your actual total amount field
        ]
        bill_table = Table(bill_summary, colWidths=[400])
        elements.append(bill_table)

        # Items purchased section
        items_data = [["Items Purchased:"]]
        headers = list(cart_items[0].keys())
        items_data.append(headers)
        for item in cart_items:
            items_data.append([item[key] for key in headers])

        items_table = Table(items_data, colWidths=[40] * len(headers))
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

    except Exception as e:
        print(f"Error generating PDF: {e}")

def calculate_grand_total(cart_items):
    total = sum(float(item['Grand Total']) for item in cart_items)
    return round(total, 2)

# Example usage
cart_items = [
    {'Item No': '1', 'Product Code': 'first product', 'HSN Code': '12', 'Sale Price': '12.0', 'Quantity': '234', 'Discount': '3', 'Amount': '2805.0', 'CGST': '168.3', 'SGST': '168.3', 'IGST': '336.6', 'Total Tax': '673.2', 'Grand Total': '3478.2', '': None},
    {'Item No': '2', 'Product Code': 'second product', 'HSN Code': '24', 'Sale Price': '15.0', 'Quantity': '200', 'Discount': '5', 'Amount': '3000.0', 'CGST': '180.0', 'SGST': '180.0', 'IGST': '360.0', 'Total Tax': '720.0', 'Grand Total': '3720.0', '': None}
]

generate_bill(cart_items)
