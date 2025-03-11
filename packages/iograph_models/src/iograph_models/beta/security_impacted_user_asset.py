from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityImpactedUserAsset(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	identifier: Optional[SecurityUserAssetIdentifier | str] = Field(alias="identifier",default=None,)

from .security_user_asset_identifier import SecurityUserAssetIdentifier

