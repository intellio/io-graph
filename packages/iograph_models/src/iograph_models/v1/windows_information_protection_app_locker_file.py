from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsInformationProtectionAppLockerFile(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	file: Optional[str] = Field(alias="file",default=None,)
	fileHash: Optional[str] = Field(alias="fileHash",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)


