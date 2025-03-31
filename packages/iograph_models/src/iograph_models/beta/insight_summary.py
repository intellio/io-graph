from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class InsightSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.insightSummary"] = Field(alias="@odata.type",)
	activeUsers: Optional[int] = Field(alias="activeUsers", default=None,)
	appId: Optional[str] = Field(alias="appId", default=None,)
	authenticationCompletions: Optional[int] = Field(alias="authenticationCompletions", default=None,)
	authenticationRequests: Optional[int] = Field(alias="authenticationRequests", default=None,)
	factDate: Optional[str] = Field(alias="factDate", default=None,)
	os: Optional[str] = Field(alias="os", default=None,)
	securityTextCompletions: Optional[int] = Field(alias="securityTextCompletions", default=None,)
	securityTextRequests: Optional[int] = Field(alias="securityTextRequests", default=None,)
	securityVoiceCompletions: Optional[int] = Field(alias="securityVoiceCompletions", default=None,)
	securityVoiceRequests: Optional[int] = Field(alias="securityVoiceRequests", default=None,)

