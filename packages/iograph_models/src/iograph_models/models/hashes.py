from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Hashes(BaseModel):
	crc32Hash: Optional[str] = Field(default=None,alias="crc32Hash",)
	quickXorHash: Optional[str] = Field(default=None,alias="quickXorHash",)
	sha1Hash: Optional[str] = Field(default=None,alias="sha1Hash",)
	sha256Hash: Optional[str] = Field(default=None,alias="sha256Hash",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


