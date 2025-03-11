from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GovernanceNotificationTemplate(BaseModel):
	culture: Optional[str] = Field(alias="culture",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	source: Optional[str] = Field(alias="source",default=None,)
	type: Optional[str] = Field(alias="type",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


