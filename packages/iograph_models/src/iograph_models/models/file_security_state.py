from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class FileSecurityState(BaseModel):
	fileHash: Optional[FileHash] = Field(default=None,alias="fileHash",)
	name: Optional[str] = Field(default=None,alias="name",)
	path: Optional[str] = Field(default=None,alias="path",)
	riskScore: Optional[str] = Field(default=None,alias="riskScore",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .file_hash import FileHash

