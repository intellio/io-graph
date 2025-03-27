from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityImpactedAssetCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[SecurityImpactedDeviceAsset, SecurityImpactedMailboxAsset, SecurityImpactedUserAsset],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .security_impacted_device_asset import SecurityImpactedDeviceAsset
from .security_impacted_mailbox_asset import SecurityImpactedMailboxAsset
from .security_impacted_user_asset import SecurityImpactedUserAsset

