from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessRelatedFile(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	directory: Optional[str] = Field(alias="directory",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	sizeInBytes: Optional[int] = Field(alias="sizeInBytes",default=None,)


