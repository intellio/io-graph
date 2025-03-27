from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConfigurationManagerClientInformation(BaseModel):
	clientIdentifier: Optional[str] = Field(alias="clientIdentifier", default=None,)
	clientVersion: Optional[str] = Field(alias="clientVersion", default=None,)
	isBlocked: Optional[bool] = Field(alias="isBlocked", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


