from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityImpactedMailboxAsset(BaseModel):
	odata_type: Literal["#microsoft.graph.security.impactedMailboxAsset"] = Field(alias="@odata.type", default="#microsoft.graph.security.impactedMailboxAsset")
	identifier: Optional[SecurityMailboxAssetIdentifier | str] = Field(alias="identifier", default=None,)

from .security_mailbox_asset_identifier import SecurityMailboxAssetIdentifier

