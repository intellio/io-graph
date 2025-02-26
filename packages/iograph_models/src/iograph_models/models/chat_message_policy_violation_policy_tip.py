from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ChatMessagePolicyViolationPolicyTip(BaseModel):
	complianceUrl: Optional[str] = Field(default=None,alias="complianceUrl",)
	generalText: Optional[str] = Field(default=None,alias="generalText",)
	matchedConditionDescriptions: list[Optional[str]] = Field(alias="matchedConditionDescriptions",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


