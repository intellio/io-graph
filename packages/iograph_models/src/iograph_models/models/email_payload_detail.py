from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EmailPayloadDetail(BaseModel):
	coachmarks: Optional[list[PayloadCoachmark]] = Field(default=None,alias="coachmarks",)
	content: Optional[str] = Field(default=None,alias="content",)
	phishingUrl: Optional[str] = Field(default=None,alias="phishingUrl",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	fromEmail: Optional[str] = Field(default=None,alias="fromEmail",)
	fromName: Optional[str] = Field(default=None,alias="fromName",)
	isExternalSender: Optional[bool] = Field(default=None,alias="isExternalSender",)
	subject: Optional[str] = Field(default=None,alias="subject",)

from .payload_coachmark import PayloadCoachmark

