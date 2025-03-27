from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserRequestsMetric(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	appId: Optional[str] = Field(alias="appId", default=None,)
	browser: Optional[str] = Field(alias="browser", default=None,)
	country: Optional[str] = Field(alias="country", default=None,)
	factDate: Optional[str] = Field(alias="factDate", default=None,)
	identityProvider: Optional[str] = Field(alias="identityProvider", default=None,)
	language: Optional[str] = Field(alias="language", default=None,)
	requestCount: Optional[int] = Field(alias="requestCount", default=None,)


