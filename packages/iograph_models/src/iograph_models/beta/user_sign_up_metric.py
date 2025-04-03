from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserSignUpMetric(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userSignUpMetric"] = Field(alias="@odata.type", default="#microsoft.graph.userSignUpMetric")
	appId: Optional[str] = Field(alias="appId", default=None,)
	browser: Optional[str] = Field(alias="browser", default=None,)
	count: Optional[int] = Field(alias="count", default=None,)
	country: Optional[str] = Field(alias="country", default=None,)
	factDate: Optional[str] = Field(alias="factDate", default=None,)
	identityProvider: Optional[str] = Field(alias="identityProvider", default=None,)
	language: Optional[str] = Field(alias="language", default=None,)
	os: Optional[str] = Field(alias="os", default=None,)

