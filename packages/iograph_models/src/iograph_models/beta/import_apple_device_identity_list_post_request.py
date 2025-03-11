from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Import_apple_device_identity_listPostRequest(BaseModel):
	importedAppleDeviceIdentities: SerializeAsAny[Optional[list[ImportedAppleDeviceIdentity]]] = Field(alias="importedAppleDeviceIdentities",default=None,)
	overwriteImportedDeviceIdentities: Optional[bool] = Field(alias="overwriteImportedDeviceIdentities",default=None,)

from .imported_apple_device_identity import ImportedAppleDeviceIdentity

