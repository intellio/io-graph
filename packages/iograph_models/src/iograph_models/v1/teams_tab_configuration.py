from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamsTabConfiguration(BaseModel):
	contentUrl: Optional[str] = Field(alias="contentUrl", default=None,)
	entityId: Optional[str] = Field(alias="entityId", default=None,)
	removeUrl: Optional[str] = Field(alias="removeUrl", default=None,)
	websiteUrl: Optional[str] = Field(alias="websiteUrl", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


