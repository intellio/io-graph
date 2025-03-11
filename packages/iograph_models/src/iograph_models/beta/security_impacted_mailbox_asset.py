from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityImpactedMailboxAsset(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	identifier: Optional[SecurityMailboxAssetIdentifier | str] = Field(alias="identifier",default=None,)

from .security_mailbox_asset_identifier import SecurityMailboxAssetIdentifier

