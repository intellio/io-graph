from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsAssignedAccessProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	appUserModelIds: Optional[list[str]] = Field(alias="appUserModelIds", default=None,)
	desktopAppPaths: Optional[list[str]] = Field(alias="desktopAppPaths", default=None,)
	profileName: Optional[str] = Field(alias="profileName", default=None,)
	showTaskBar: Optional[bool] = Field(alias="showTaskBar", default=None,)
	startMenuLayoutXml: Optional[str] = Field(alias="startMenuLayoutXml", default=None,)
	userAccounts: Optional[list[str]] = Field(alias="userAccounts", default=None,)


