from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Hashes(BaseModel):
	crc32Hash: Optional[str] = Field(alias="crc32Hash",default=None,)
	quickXorHash: Optional[str] = Field(alias="quickXorHash",default=None,)
	sha1Hash: Optional[str] = Field(alias="sha1Hash",default=None,)
	sha256Hash: Optional[str] = Field(alias="sha256Hash",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


