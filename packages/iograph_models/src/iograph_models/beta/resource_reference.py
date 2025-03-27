from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ResourceReference(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


