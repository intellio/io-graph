from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LinkedResource(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	applicationName: Optional[str] = Field(alias="applicationName",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	externalId: Optional[str] = Field(alias="externalId",default=None,)
	webUrl: Optional[str] = Field(alias="webUrl",default=None,)


