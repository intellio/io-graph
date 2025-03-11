from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CustomClaimCondition(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	memberOf: Optional[list[str]] = Field(alias="memberOf",default=None,)
	userType: Optional[ClaimConditionUserType | str] = Field(alias="userType",default=None,)

from .claim_condition_user_type import ClaimConditionUserType

