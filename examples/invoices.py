import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import shippo

print(shippo.Invoice.all(api_key="<API-KEY>", size=20, page=1))

print(shippo.InvoiceItem.all(api_key="<API-KEY>", invoiceObjectId='insert invoice object id'))