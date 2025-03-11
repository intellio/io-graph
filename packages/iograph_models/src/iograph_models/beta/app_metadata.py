from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppMetadata(BaseModel):
	data: Optional[list[AppMetadataEntry]] = Field(alias="data",default=None,)
	version: Optional[int] = Field(alias="version",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .app_metadata_entry import AppMetadataEntry

