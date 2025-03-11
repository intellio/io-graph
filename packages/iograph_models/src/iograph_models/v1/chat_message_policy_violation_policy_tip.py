from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ChatMessagePolicyViolationPolicyTip(BaseModel):
	complianceUrl: Optional[str] = Field(alias="complianceUrl",default=None,)
	generalText: Optional[str] = Field(alias="generalText",default=None,)
	matchedConditionDescriptions: Optional[list[str]] = Field(alias="matchedConditionDescriptions",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


