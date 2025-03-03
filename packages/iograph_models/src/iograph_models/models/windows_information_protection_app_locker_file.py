from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsInformationProtectionAppLockerFile(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	file: Optional[str] = Field(default=None,alias="file",)
	fileHash: Optional[str] = Field(default=None,alias="fileHash",)
	version: Optional[str] = Field(default=None,alias="version",)


