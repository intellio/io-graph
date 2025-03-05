from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LinkedResource(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	applicationName: Optional[str] = Field(default=None,alias="applicationName",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	externalId: Optional[str] = Field(default=None,alias="externalId",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)


