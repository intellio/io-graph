from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityImpactedDeviceAsset(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	identifier: Optional[SecurityDeviceAssetIdentifier | str] = Field(alias="identifier",default=None,)

from .security_device_asset_identifier import SecurityDeviceAssetIdentifier

