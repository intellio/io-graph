from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class MfaCompletionMetric(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.mfaCompletionMetric"] = Field(alias="@odata.type", default="#microsoft.graph.mfaCompletionMetric")
	appId: Optional[str] = Field(alias="appId", default=None,)
	attemptsCount: Optional[int] = Field(alias="attemptsCount", default=None,)
	country: Optional[str] = Field(alias="country", default=None,)
	factDate: Optional[str] = Field(alias="factDate", default=None,)
	identityProvider: Optional[str] = Field(alias="identityProvider", default=None,)
	language: Optional[str] = Field(alias="language", default=None,)
	mfaMethod: Optional[str] = Field(alias="mfaMethod", default=None,)
	os: Optional[str] = Field(alias="os", default=None,)
	successCount: Optional[int] = Field(alias="successCount", default=None,)
	mfaFailures: Optional[list[MfaFailure]] = Field(alias="mfaFailures", default=None,)

from .mfa_failure import MfaFailure
