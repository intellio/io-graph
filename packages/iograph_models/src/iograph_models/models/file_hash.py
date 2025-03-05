from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FileHash(BaseModel):
	hashType: Optional[str | FileHashType] = Field(alias="hashType",default=None,)
	hashValue: Optional[str] = Field(alias="hashValue",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .file_hash_type import FileHashType

