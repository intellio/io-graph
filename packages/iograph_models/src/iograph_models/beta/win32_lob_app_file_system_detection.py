from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobAppFileSystemDetection(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	check32BitOn64System: Optional[bool] = Field(alias="check32BitOn64System",default=None,)
	detectionType: Optional[Win32LobAppFileSystemDetectionType | str] = Field(alias="detectionType",default=None,)
	detectionValue: Optional[str] = Field(alias="detectionValue",default=None,)
	fileOrFolderName: Optional[str] = Field(alias="fileOrFolderName",default=None,)
	operator: Optional[Win32LobAppDetectionOperator | str] = Field(alias="operator",default=None,)
	path: Optional[str] = Field(alias="path",default=None,)

from .win32_lob_app_file_system_detection_type import Win32LobAppFileSystemDetectionType
from .win32_lob_app_detection_operator import Win32LobAppDetectionOperator

