from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OnlineMeetingInfo(BaseModel):
	conferenceId: Optional[str] = Field(default=None,alias="conferenceId",)
	joinUrl: Optional[str] = Field(default=None,alias="joinUrl",)
	phones: list[Phone] = Field(alias="phones",)
	quickDial: Optional[str] = Field(default=None,alias="quickDial",)
	tollFreeNumbers: list[Optional[str]] = Field(alias="tollFreeNumbers",)
	tollNumber: Optional[str] = Field(default=None,alias="tollNumber",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .phone import Phone

