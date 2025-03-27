from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityImpactedUserAsset(BaseModel):
	odata_type: Literal["#microsoft.graph.security.impactedUserAsset"] = Field(alias="@odata.type", default="#microsoft.graph.security.impactedUserAsset")
	identifier: Optional[SecurityUserAssetIdentifier | str] = Field(alias="identifier", default=None,)

from .security_user_asset_identifier import SecurityUserAssetIdentifier

