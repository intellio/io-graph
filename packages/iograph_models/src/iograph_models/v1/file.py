from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class File(BaseModel):
	hashes: Optional[Hashes] = Field(alias="hashes", default=None,)
	mimeType: Optional[str] = Field(alias="mimeType", default=None,)
	processingMetadata: Optional[bool] = Field(alias="processingMetadata", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .hashes import Hashes

