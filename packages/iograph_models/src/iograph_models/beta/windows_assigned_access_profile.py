from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WindowsAssignedAccessProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsAssignedAccessProfile"] = Field(alias="@odata.type", default="#microsoft.graph.windowsAssignedAccessProfile")
	appUserModelIds: Optional[list[str]] = Field(alias="appUserModelIds", default=None,)
	desktopAppPaths: Optional[list[str]] = Field(alias="desktopAppPaths", default=None,)
	profileName: Optional[str] = Field(alias="profileName", default=None,)
	showTaskBar: Optional[bool] = Field(alias="showTaskBar", default=None,)
	startMenuLayoutXml: Optional[str] = Field(alias="startMenuLayoutXml", default=None,)
	userAccounts: Optional[list[str]] = Field(alias="userAccounts", default=None,)

