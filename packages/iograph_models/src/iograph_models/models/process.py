from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Process(BaseModel):
	accountName: Optional[str] = Field(default=None,alias="accountName",)
	commandLine: Optional[str] = Field(default=None,alias="commandLine",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	fileHash: Optional[FileHash] = Field(default=None,alias="fileHash",)
	integrityLevel: Optional[ProcessIntegrityLevel] = Field(default=None,alias="integrityLevel",)
	isElevated: Optional[bool] = Field(default=None,alias="isElevated",)
	name: Optional[str] = Field(default=None,alias="name",)
	parentProcessCreatedDateTime: Optional[datetime] = Field(default=None,alias="parentProcessCreatedDateTime",)
	parentProcessId: Optional[int] = Field(default=None,alias="parentProcessId",)
	parentProcessName: Optional[str] = Field(default=None,alias="parentProcessName",)
	path: Optional[str] = Field(default=None,alias="path",)
	processId: Optional[int] = Field(default=None,alias="processId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .file_hash import FileHash
from .process_integrity_level import ProcessIntegrityLevel

