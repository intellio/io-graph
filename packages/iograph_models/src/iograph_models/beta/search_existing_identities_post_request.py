from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Search_existing_identitiesPostRequest(BaseModel):
	importedDeviceIdentities: SerializeAsAny[Optional[list[ImportedDeviceIdentity]]] = Field(alias="importedDeviceIdentities",default=None,)

from .imported_device_identity import ImportedDeviceIdentity

