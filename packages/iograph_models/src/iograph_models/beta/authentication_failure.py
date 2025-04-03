from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AuthenticationFailure(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.authenticationFailure"] = Field(alias="@odata.type", default="#microsoft.graph.authenticationFailure")
	count: Optional[int] = Field(alias="count", default=None,)
	reason: Optional[str] = Field(alias="reason", default=None,)
	reasonCode: Optional[AuthenticationFailureReasonCode | str] = Field(alias="reasonCode", default=None,)

from .authentication_failure_reason_code import AuthenticationFailureReasonCode
