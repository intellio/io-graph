from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Win32LobAppFileSystemRequirement(BaseModel):
	detectionValue: Optional[str] = Field(alias="detectionValue", default=None,)
	operator: Optional[Win32LobAppDetectionOperator | str] = Field(alias="operator", default=None,)
	odata_type: Literal["#microsoft.graph.win32LobAppFileSystemRequirement"] = Field(alias="@odata.type", default="#microsoft.graph.win32LobAppFileSystemRequirement")
	check32BitOn64System: Optional[bool] = Field(alias="check32BitOn64System", default=None,)
	detectionType: Optional[Win32LobAppFileSystemDetectionType | str] = Field(alias="detectionType", default=None,)
	fileOrFolderName: Optional[str] = Field(alias="fileOrFolderName", default=None,)
	path: Optional[str] = Field(alias="path", default=None,)

from .win32_lob_app_detection_operator import Win32LobAppDetectionOperator
from .win32_lob_app_file_system_detection_type import Win32LobAppFileSystemDetectionType
