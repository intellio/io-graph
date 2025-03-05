from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TelecomExpenseManagementPartnerCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[TelecomExpenseManagementPartner]] = Field(alias="value",default=None,)

from .telecom_expense_management_partner import TelecomExpenseManagementPartner

