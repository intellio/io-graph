from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityAnalyzedEmailExchangeTransportRuleInfo(BaseModel):
	name: Optional[str] = Field(alias="name", default=None,)
	ruleId: Optional[str] = Field(alias="ruleId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


