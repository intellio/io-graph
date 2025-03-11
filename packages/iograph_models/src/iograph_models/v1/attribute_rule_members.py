from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AttributeRuleMembers(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	membershipRule: Optional[str] = Field(alias="membershipRule",default=None,)


