from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnlineMeetingInfo(BaseModel):
	conferenceId: Optional[str] = Field(default=None,alias="conferenceId",)
	joinUrl: Optional[str] = Field(default=None,alias="joinUrl",)
	phones: Optional[list[Phone]] = Field(default=None,alias="phones",)
	quickDial: Optional[str] = Field(default=None,alias="quickDial",)
	tollFreeNumbers: Optional[list[str]] = Field(default=None,alias="tollFreeNumbers",)
	tollNumber: Optional[str] = Field(default=None,alias="tollNumber",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .phone import Phone

