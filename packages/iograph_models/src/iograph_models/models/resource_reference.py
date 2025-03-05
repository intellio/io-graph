from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ResourceReference(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	type: Optional[str] = Field(default=None,alias="type",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


