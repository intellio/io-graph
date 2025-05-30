from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class IndustryDataOAuth2ClientCredential(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isValid: Optional[bool] = Field(alias="isValid", default=None,)
	lastValidDateTime: Optional[datetime] = Field(alias="lastValidDateTime", default=None,)
	odata_type: Literal["#microsoft.graph.industryData.oAuth2ClientCredential"] = Field(alias="@odata.type", default="#microsoft.graph.industryData.oAuth2ClientCredential")
	clientId: Optional[str] = Field(alias="clientId", default=None,)
	clientSecret: Optional[str] = Field(alias="clientSecret", default=None,)
	scope: Optional[str] = Field(alias="scope", default=None,)
	tokenUrl: Optional[str] = Field(alias="tokenUrl", default=None,)

