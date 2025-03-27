from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Enable_lost_modePostRequest(BaseModel):
	message: Optional[str] = Field(alias="message", default=None,)
	phoneNumber: Optional[str] = Field(alias="phoneNumber", default=None,)
	footer: Optional[str] = Field(alias="footer", default=None,)


