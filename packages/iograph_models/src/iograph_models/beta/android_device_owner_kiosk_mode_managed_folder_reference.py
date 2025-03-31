from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AndroidDeviceOwnerKioskModeManagedFolderReference(BaseModel):
	odata_type: Literal["#microsoft.graph.androidDeviceOwnerKioskModeManagedFolderReference"] = Field(alias="@odata.type", default="#microsoft.graph.androidDeviceOwnerKioskModeManagedFolderReference")
	folderIdentifier: Optional[str] = Field(alias="folderIdentifier", default=None,)
	folderName: Optional[str] = Field(alias="folderName", default=None,)

