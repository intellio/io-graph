from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class FileSecurityState(BaseModel):
	fileHash: Optional[FileHash] = Field(alias="fileHash", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	path: Optional[str] = Field(alias="path", default=None,)
	riskScore: Optional[str] = Field(alias="riskScore", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .file_hash import FileHash
