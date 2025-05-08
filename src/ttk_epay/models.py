# models.py
class Invoice:
    def __init__(
        self,
        ID: int,
        INVOICE_NUMBER: int = None,
        ORDER_ID: str = None,
        INVOICE_DATE: str = None,  # ISO 8601 datetime string, e.g., "2025-05-07T12:45:27.142Z"
        INVOICE_TYPE_CODE: str = None,
        NET_AMOUNT: float = None,
        INVOICE_TVA: float = None,
        AMOUNT_TVA: float = None,
        AMOUNT_TTC: float = None,
        INVOICE_STATE_CODE: str = None,
        ORDER_NAME: str = None,
        CLIENT_CODE: int = None,
        CLIENT_NAME: str = None,
        CLIENT_NRC: str = None,
        CLIENT_ADDRESS: str = None,
        CLIENT_MAIL: str = None,
        CLIENT_IDF: str = None,
        PRODUCT_NAME: str = None,
        IS_PAID: bool = False
    ):
        """
        INVOICE object.

        Fields:
        - ID (int): Required.
        - INVOICE_NUMBER (int, optional): Nullable.
        - ORDER_ID (str, optional): Nullable.
        - INVOICE_DATE (str, optional): ISO 8601 date-time format.
        - INVOICE_TYPE_CODE (str, optional): Nullable.
        - NET_AMOUNT (float, optional): Nullable, double.
        - INVOICE_TVA (float, optional): Nullable, double.
        - AMOUNT_TVA (float, optional): Nullable, double.
        - AMOUNT_TTC (float, optional): Nullable, double.
        - INVOICE_STATE_CODE (str, optional): Nullable.
        - ORDER_NAME (str, optional): Nullable.
        - CLIENT_CODE (int, optional): Nullable.
        - CLIENT_NAME (str, optional): Nullable.
        - CLIENT_NRC (str, optional): Nullable.
        - CLIENT_ADDRESS (str, optional): Nullable.
        - CLIENT_MAIL (str, optional): Nullable.
        - CLIENT_IDF (str, optional): Nullable.
        - PRODUCT_NAME (str, optional): Nullable.
        - IS_PAID (bool): Required, default False.
        """
        self.ID = ID
        self.INVOICE_NUMBER = INVOICE_NUMBER
        self.ORDER_ID = ORDER_ID
        self.INVOICE_DATE = INVOICE_DATE
        self.INVOICE_TYPE_CODE = INVOICE_TYPE_CODE
        self.NET_AMOUNT = NET_AMOUNT
        self.INVOICE_TVA = INVOICE_TVA
        self.AMOUNT_TVA = AMOUNT_TVA
        self.AMOUNT_TTC = AMOUNT_TTC
        self.INVOICE_STATE_CODE = INVOICE_STATE_CODE
        self.ORDER_NAME = ORDER_NAME
        self.CLIENT_CODE = CLIENT_CODE
        self.CLIENT_NAME = CLIENT_NAME
        self.CLIENT_NRC = CLIENT_NRC
        self.CLIENT_ADDRESS = CLIENT_ADDRESS
        self.CLIENT_MAIL = CLIENT_MAIL
        self.CLIENT_IDF = CLIENT_IDF
        self.PRODUCT_NAME = PRODUCT_NAME
        self.IS_PAID = IS_PAID


class InvoiceDto:
    def __init__(
        self,
        INVOICE_NUMBER: int,
        ORDER_ID: str = None,
        INVOICE_DATE: str = None,  # ISO 8601 datetime string
        INVOICE_TYPE_CODE: str = None,
        NET_AMOUNT: float = None,
        CLIENT_CODE: int = None,
        CLIENT_NAME: str = None,
        CLIENT_ADDRESS: str = None,
        CLIENT_MAIL: str = None,
        PRODUCT_NAME: str = None
    ):
        """
        InvoiceDto object.

        Fields:
        - INVOICE_NUMBER (int): Required.
        - ORDER_ID (str, optional): Nullable.
        - INVOICE_DATE (str, optional): ISO 8601 date-time format.
        - INVOICE_TYPE_CODE (str, optional): Nullable.
        - NET_AMOUNT (float, optional): Nullable, double.
        - CLIENT_CODE (int, optional): Nullable.
        - CLIENT_NAME (str, optional): Nullable.
        - CLIENT_ADDRESS (str, optional): Nullable.
        - CLIENT_MAIL (str, optional): Nullable.
        - PRODUCT_NAME (str, optional): Nullable.
        """
        self.INVOICE_NUMBER = INVOICE_NUMBER
        self.ORDER_ID = ORDER_ID
        self.INVOICE_DATE = INVOICE_DATE
        self.INVOICE_TYPE_CODE = INVOICE_TYPE_CODE
        self.NET_AMOUNT = NET_AMOUNT
        self.CLIENT_CODE = CLIENT_CODE
        self.CLIENT_NAME = CLIENT_NAME
        self.CLIENT_ADDRESS = CLIENT_ADDRESS
        self.CLIENT_MAIL = CLIENT_MAIL
        self.PRODUCT_NAME = PRODUCT_NAME
