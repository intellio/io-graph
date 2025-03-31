from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class MfaFailure(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.mfaFailure"] = Field(alias="@odata.type",)
	count: Optional[int] = Field(alias="count", default=None,)
	reason: Optional[str] = Field(alias="reason", default=None,)
	reasonCode: Optional[MfaFailureReasonCode | str] = Field(alias="reasonCode", default=None,)

from .mfa_failure_reason_code import MfaFailureReasonCode
