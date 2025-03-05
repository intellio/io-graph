from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FileHash(BaseModel):
	hashType: Optional[FileHashType] = Field(default=None,alias="hashType",)
	hashValue: Optional[str] = Field(default=None,alias="hashValue",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .file_hash_type import FileHashType

