from __future__ import annotations
from enum import StrEnum


class ContentModelType(StrEnum):
	teachingMethod = "teachingMethod"
	layoutMethod = "layoutMethod"
	freeformSelectionMethod = "freeformSelectionMethod"
	prebuiltContractModel = "prebuiltContractModel"
	prebuiltInvoiceModel = "prebuiltInvoiceModel"
	prebuiltReceiptModel = "prebuiltReceiptModel"
	unknownFutureValue = "unknownFutureValue"

