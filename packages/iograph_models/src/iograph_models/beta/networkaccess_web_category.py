from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessWebCategory(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	group: Optional[str] = Field(alias="group",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)


