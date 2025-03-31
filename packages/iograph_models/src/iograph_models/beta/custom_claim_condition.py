from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CustomClaimCondition(BaseModel):
	odata_type: Literal["#microsoft.graph.customClaimCondition"] = Field(alias="@odata.type", default="#microsoft.graph.customClaimCondition")
	memberOf: Optional[list[str]] = Field(alias="memberOf", default=None,)
	userType: Optional[ClaimConditionUserType | str] = Field(alias="userType", default=None,)

from .claim_condition_user_type import ClaimConditionUserType
