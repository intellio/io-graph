from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Process(BaseModel):
	accountName: Optional[str] = Field(alias="accountName",default=None,)
	commandLine: Optional[str] = Field(alias="commandLine",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	fileHash: Optional[FileHash] = Field(alias="fileHash",default=None,)
	integrityLevel: Optional[ProcessIntegrityLevel | str] = Field(alias="integrityLevel",default=None,)
	isElevated: Optional[bool] = Field(alias="isElevated",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	parentProcessCreatedDateTime: Optional[datetime] = Field(alias="parentProcessCreatedDateTime",default=None,)
	parentProcessId: Optional[int] = Field(alias="parentProcessId",default=None,)
	parentProcessName: Optional[str] = Field(alias="parentProcessName",default=None,)
	path: Optional[str] = Field(alias="path",default=None,)
	processId: Optional[int] = Field(alias="processId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .file_hash import FileHash
from .process_integrity_level import ProcessIntegrityLevel

