from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessRelatedTransaction(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	transactionId: Optional[str] = Field(alias="transactionId",default=None,)


