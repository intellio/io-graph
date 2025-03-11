from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Self_activatePostRequest(BaseModel):
	reason: Optional[str] = Field(alias="reason",default=None,)
	duration: Optional[str] = Field(alias="duration",default=None,)
	ticketNumber: Optional[str] = Field(alias="ticketNumber",default=None,)
	ticketSystem: Optional[str] = Field(alias="ticketSystem",default=None,)


