from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WindowsInformationProtectionDesktopApp(BaseModel):
	denied: Optional[bool] = Field(alias="denied", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	productName: Optional[str] = Field(alias="productName", default=None,)
	publisherName: Optional[str] = Field(alias="publisherName", default=None,)
	odata_type: Literal["#microsoft.graph.windowsInformationProtectionDesktopApp"] = Field(alias="@odata.type", default="#microsoft.graph.windowsInformationProtectionDesktopApp")
	binaryName: Optional[str] = Field(alias="binaryName", default=None,)
	binaryVersionHigh: Optional[str] = Field(alias="binaryVersionHigh", default=None,)
	binaryVersionLow: Optional[str] = Field(alias="binaryVersionLow", default=None,)

