# app.py
import requests
import logging
from .models import Invoice, InvoiceDto

BASE_URL = "https://pay.deploily.cloud/api/v1"

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ttk_epay:
    """
    A class to represent the ttk_epay application.
    """

    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(
            {"Accept": "*/*", "Content-Type": "application/json"}
        )

    # ===============
    # Admin
    # ===============

    def get_invoices(self, page_number: int = 1, page_size: int = 10) -> dict:
        """
        Get a paginated list of invoices from the API.

        Args:
            page_number: The page number to retrieve (1-based index). Defaults to 1.
            page_size: The number of invoices to return per page. Defaults to 10.

        Returns:
            dict: A dictionary containing:
                - List of Invoice objects
                - "CURRENTPAGE": Current page number (int)
                - "TOTALPAGES": Total pages available (int)
        """
        url = f"{self.base_url}/admin/invoices"
        params = {"pageNumber": page_number, "pageSize": page_size}
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error occurred: {e}")
            logger.error(f"Response status code: {response.status_code}")
            logger.error(f"Response body: {response.text}")
            raise

    def create_invoice(self, invoice_data: Invoice) -> dict:
        """
        Create a new invoice.

        Args:
            invoice_data (Invoice): Invoice object.

        Returns:
            dict (Invoice): The created Invoice object.
        """
        url = f"{self.base_url}/admin/invoices"
        try:
            response = self.session.post(url, json=invoice_data.__dict__)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error occurred: {e}")
            logger.error(f"Response status code: {response.status_code}")
            logger.error(f"Response body: {response.text}")
            raise

    # TODO: Fix the bug here (when invoice is not found)
    def get_invoice_by_order_id(self, order_id: str):
        """
        Get details of a specific invoice by the order ID.

        Args:
            order_id (str): The order ID of the invoice to retrieve.

        Returns:
            dict (Invoice): The created Invoice object.
        """
        url = f"{self.base_url}/admin/invoices/{order_id}"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.RequestException as e:
            logger.error(f"Error fetching invoice with order ID {order_id}: {e}")
            logger.error(f"HTTP error occurred: {e}")
            logger.error(f"Response status code: {response.status_code}")
            logger.error(f"Response body: {response.text}")
            raise

    def update_invoice(self, invoice_id: int, invoice_data: Invoice):
        """
        Update an invoice by ID with the provided invoice_data (as dict).

        Args:
            invoice_id (int): The ID of the invoice to update.
            invoice_data (Invoice): Invoice object.

        Returns:
            dict (Invoice): The updated Invoice object.
        """
        url = f"{self.base_url}/admin/invoices/{invoice_id}"
        try:
            response = self.session.patch(url, json=invoice_data.__dict__)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error updating invoice with invoice ID {invoice_id}: {e}")
            logger.error(f"HTTP error occurred: {e}")
            logger.error(f"Response status code: {response.status_code}")
            logger.error(f"Response body: {response.text}")
            raise

    def get_payments(
        self,
        page_number: int = None,
        page_size: int = None,
        satim_order_id: str = None,
        invoice_id: str = None,
        from_date: str = None,
        to_date: str = None,
    ):
        """
        Get list of payments with optional filtering parameters.

        Args:
            page_number: Page number for pagination (default: 1)
            page_size: Number of items per page (default: 10)
            satim_order_id: Filter by Satim order ID
            invoice_id: Filter by invoice ID
            from_date: Start date filter (format: 'YYYY-MM-DDTHH:MM:SSZ')
            to_date: End date filter (format: 'YYYY-MM-DDTHH:MM:SSZ')

        Returns:
            JSON response with payments or None if error occurs
        """
        params = {}
        if page_number:
            params["pageNumber"] = page_number
        if page_size:
            params["pageSize"] = page_size
        if satim_order_id:
            params["SatimOrderId"] = satim_order_id
        if invoice_id:
            params["InvoiceId"] = invoice_id
        if from_date:
            params["FromDate"] = from_date
        if to_date:
            params["toDate"] = to_date

        url = f"{self.base_url}/admin/payments"
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error fetching payments: {e}")
            raise

    # ================
    # File
    # ================

    def get_pdf_recipt(self, satim_order_id: str):
        """
        Get the PDF receipt for a specific invoice.

        Args:
            invoice_id (str): The ID of the invoice.

        Returns:
            bytes: The PDF receipt as bytes.
        """
        url = f"{self.base_url}/epayment/generate-pdf"
        try:
            response = self.session.get(url, params={"SATIM_ORDER_ID": satim_order_id})
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            logger.error(
                f"Error fetching PDF receipt for invoice with satim_order_id: {satim_order_id}: {e}"
            )
            raise

    def send_pdf_recipt_mail(self, satim_order_id: str, email: str):
        """
        Send the PDF receipt to a specific email address.

        Args:
            satim_order_id (str): The ID of the invoice.
            email (str): The email address to send the receipt to.

        Returns:
            The response from the API.
        """
        url = f"{self.base_url}/epayment/send-mail"
        try:
            response = self.session.get(
                url, params={"SATIM_ORDER_ID": satim_order_id, "EMAIL": email}
            )
            response.raise_for_status()
            content_type = response.headers.get("Content-Type")
            if content_type == "application/json":
                return response.json()
            return response.text

        except requests.RequestException as e:
            logger.error(f"Response status code: {response.status_code}")
            logger.error(
                f"Error sending PDF receipt for invoice with satim_order_id: {satim_order_id} to {email}: {e}"
            )
            raise

    # ================
    # User
    # ================
    
    # TODO: A bug here to fix
    def post_payement(self, payment_data: InvoiceDto):
        """
        Post a payment to the API.

        Args:
            payment_data (InvoiceDto): Payment data object.

        Returns:
            dict: The created payment object.
        """
        url = f"{self.base_url}/epayment"
        try:
            response = self.session.post(url, json=payment_data.__dict__)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error posting payment: {e}")
            raise

    def get_payment_status(self, satim_order_id: str):
        """
        Get the payment status for a specific invoice.

        Args:
            satim_order_id (str): The ID of the invoice.

        Returns:
            dict: The payment status.
        """
        url = f"{self.base_url}/epayment"
        try:
            response = self.session.get(url, params={"SATIM_ORDER_ID": satim_order_id})
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error fetching payment status: {e}")
            raise
