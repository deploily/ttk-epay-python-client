# ttk-epay-python-client

# Welcome to Python Package Repository
# for [TTK ePay](https://pay.deploily.cloud) Payment Gateway

This package is developed by **Charen Bahaeddine Hemmem ([1hemmem](https://github.com/1hemmem))** and is open to contributions from developers like you.

## Requirements
TTK ePay requires `Python 3.8` and above.

## Installation
```bash
pip install ttk-epay
```

## Usage
```python
from ttk_epay import ttk_epay
from ttk_epay.models import Invoice, InvoiceDto

# Initialize the client
client = ttk_epay(base_url="https://pay.deploily.cloud/api/v1")

# ==============
# Invoice Management
# ==============

# Create an invoice
invoice_data = Invoice(
    ID=123,
    INVOICE_NUMBER=456,
    NET_AMOUNT=100.0,
    CLIENT_NAME="Client name",
    CLIENT_MAIL="client@example.com"
)
created_invoice = client.create_invoice(invoice_data)

# Get paginated invoices
invoices = client.get_invoices(page_number=1, page_size=10)

# Get invoice by order ID
invoice = client.get_invoice_by_order_id("41")

# ==============
# Receipt Management
# ==============

# Get PDF receipt
pdf_response = client.get_pdf_recipt("8LmjDNjisi0A5EAAGBYM")
with open("receipt.pdf", "wb") as f:
    f.write(pdf_response.content)

# Send receipt via email
result = client.send_pdf_recipt_mail("8LmjDNjisi0A5EAAGBYM", "client@example.com")

# ==============
# Payment Processing
# ==============

# Create a payment
payment_data = InvoiceDto(
    INVOICE_NUMBER=456,
    NET_AMOUNT=100.0,
    CLIENT_NAME="John Doe"
)
payment = client.post_payement(payment_data)

# Check payment status
status = client.get_payment_status("8LmjDNjisi0A5EAAGBYM")

```
