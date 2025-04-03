from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AuthenticationsMetric(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.authenticationsMetric"] = Field(alias="@odata.type", default="#microsoft.graph.authenticationsMetric")
	appid: Optional[str] = Field(alias="appid", default=None,)
	attemptsCount: Optional[int] = Field(alias="attemptsCount", default=None,)
	authFlow: Optional[str] = Field(alias="authFlow", default=None,)
	browser: Optional[str] = Field(alias="browser", default=None,)
	country: Optional[str] = Field(alias="country", default=None,)
	factDate: Optional[str] = Field(alias="factDate", default=None,)
	identityProvider: Optional[str] = Field(alias="identityProvider", default=None,)
	language: Optional[str] = Field(alias="language", default=None,)
	os: Optional[str] = Field(alias="os", default=None,)
	successCount: Optional[int] = Field(alias="successCount", default=None,)
	failures: Optional[list[AuthenticationFailure]] = Field(alias="failures", default=None,)

from .authentication_failure import AuthenticationFailure
