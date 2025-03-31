from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class GeneralLedgerEntryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[GeneralLedgerEntry]] = Field(alias="value", default=None,)

from .general_ledger_entry import GeneralLedgerEntry
