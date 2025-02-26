from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TicketInfo(BaseModel):
	ticketNumber: Optional[str] = Field(default=None,alias="ticketNumber",)
	ticketSystem: Optional[str] = Field(default=None,alias="ticketSystem",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


