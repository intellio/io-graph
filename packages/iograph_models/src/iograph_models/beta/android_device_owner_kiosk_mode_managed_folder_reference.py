from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidDeviceOwnerKioskModeManagedFolderReference(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	folderIdentifier: Optional[str] = Field(alias="folderIdentifier",default=None,)
	folderName: Optional[str] = Field(alias="folderName",default=None,)


