from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class EmailPayloadDetail(BaseModel):
	coachmarks: Optional[list[PayloadCoachmark]] = Field(alias="coachmarks", default=None,)
	content: Optional[str] = Field(alias="content", default=None,)
	phishingUrl: Optional[str] = Field(alias="phishingUrl", default=None,)
	odata_type: Literal["#microsoft.graph.emailPayloadDetail"] = Field(alias="@odata.type", default="#microsoft.graph.emailPayloadDetail")
	fromEmail: Optional[str] = Field(alias="fromEmail", default=None,)
	fromName: Optional[str] = Field(alias="fromName", default=None,)
	isExternalSender: Optional[bool] = Field(alias="isExternalSender", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)

from .payload_coachmark import PayloadCoachmark
