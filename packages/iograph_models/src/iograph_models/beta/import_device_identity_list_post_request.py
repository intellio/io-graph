from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Import_device_identity_listPostRequest(BaseModel):
	importedDeviceIdentities: SerializeAsAny[Optional[list[ImportedDeviceIdentity]]] = Field(alias="importedDeviceIdentities",default=None,)
	overwriteImportedDeviceIdentities: Optional[bool] = Field(alias="overwriteImportedDeviceIdentities",default=None,)

from .imported_device_identity import ImportedDeviceIdentity

