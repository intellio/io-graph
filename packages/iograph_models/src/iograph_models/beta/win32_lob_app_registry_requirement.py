from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Win32LobAppRegistryRequirement(BaseModel):
	detectionValue: Optional[str] = Field(alias="detectionValue", default=None,)
	operator: Optional[Win32LobAppDetectionOperator | str] = Field(alias="operator", default=None,)
	odata_type: Literal["#microsoft.graph.win32LobAppRegistryRequirement"] = Field(alias="@odata.type", default="#microsoft.graph.win32LobAppRegistryRequirement")
	check32BitOn64System: Optional[bool] = Field(alias="check32BitOn64System", default=None,)
	detectionType: Optional[Win32LobAppRegistryDetectionType | str] = Field(alias="detectionType", default=None,)
	keyPath: Optional[str] = Field(alias="keyPath", default=None,)
	valueName: Optional[str] = Field(alias="valueName", default=None,)

from .win32_lob_app_detection_operator import Win32LobAppDetectionOperator
from .win32_lob_app_registry_detection_type import Win32LobAppRegistryDetectionType
