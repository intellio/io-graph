from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnlineMeetingInfo(BaseModel):
	conferenceId: Optional[str] = Field(alias="conferenceId", default=None,)
	joinUrl: Optional[str] = Field(alias="joinUrl", default=None,)
	phones: Optional[list[Phone]] = Field(alias="phones", default=None,)
	quickDial: Optional[str] = Field(alias="quickDial", default=None,)
	tollFreeNumbers: Optional[list[str]] = Field(alias="tollFreeNumbers", default=None,)
	tollNumber: Optional[str] = Field(alias="tollNumber", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .phone import Phone

