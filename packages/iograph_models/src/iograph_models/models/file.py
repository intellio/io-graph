from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class File(BaseModel):
	hashes: Optional[Hashes] = Field(default=None,alias="hashes",)
	mimeType: Optional[str] = Field(default=None,alias="mimeType",)
	processingMetadata: Optional[bool] = Field(default=None,alias="processingMetadata",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .hashes import Hashes

