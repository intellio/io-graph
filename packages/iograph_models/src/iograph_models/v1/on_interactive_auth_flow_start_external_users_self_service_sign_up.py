from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class OnInteractiveAuthFlowStartExternalUsersSelfServiceSignUp(BaseModel):
	odata_type: Literal["#microsoft.graph.onInteractiveAuthFlowStartExternalUsersSelfServiceSignUp"] = Field(alias="@odata.type", default="#microsoft.graph.onInteractiveAuthFlowStartExternalUsersSelfServiceSignUp")
	isSignUpAllowed: Optional[bool] = Field(alias="isSignUpAllowed", default=None,)

