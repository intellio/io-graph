from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AgedAccountsReceivableCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AgedAccountsReceivable]] = Field(alias="value", default=None,)

from .aged_accounts_receivable import AgedAccountsReceivable

