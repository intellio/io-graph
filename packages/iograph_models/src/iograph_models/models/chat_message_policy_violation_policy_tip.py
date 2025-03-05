from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChatMessagePolicyViolationPolicyTip(BaseModel):
	complianceUrl: Optional[str] = Field(default=None,alias="complianceUrl",)
	generalText: Optional[str] = Field(default=None,alias="generalText",)
	matchedConditionDescriptions: Optional[list[str]] = Field(default=None,alias="matchedConditionDescriptions",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


