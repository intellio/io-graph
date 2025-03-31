from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ExchangeSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.exchangeSettings"] = Field(alias="@odata.type",)
	inPlaceArchiveMailboxId: Optional[str] = Field(alias="inPlaceArchiveMailboxId", default=None,)
	primaryMailboxId: Optional[str] = Field(alias="primaryMailboxId", default=None,)

