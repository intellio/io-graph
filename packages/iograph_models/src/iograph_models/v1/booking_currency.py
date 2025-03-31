from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class BookingCurrency(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.bookingCurrency"] = Field(alias="@odata.type",)
	symbol: Optional[str] = Field(alias="symbol", default=None,)

