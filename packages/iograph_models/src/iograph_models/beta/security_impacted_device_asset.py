from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityImpactedDeviceAsset(BaseModel):
	odata_type: Literal["#microsoft.graph.security.impactedDeviceAsset"] = Field(alias="@odata.type", default="#microsoft.graph.security.impactedDeviceAsset")
	identifier: Optional[SecurityDeviceAssetIdentifier | str] = Field(alias="identifier", default=None,)

from .security_device_asset_identifier import SecurityDeviceAssetIdentifier

