from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Make_permanentPostRequest(BaseModel):
	reason: Optional[str] = Field(alias="reason", default=None,)
	ticketNumber: Optional[str] = Field(alias="ticketNumber", default=None,)
	ticketSystem: Optional[str] = Field(alias="ticketSystem", default=None,)


