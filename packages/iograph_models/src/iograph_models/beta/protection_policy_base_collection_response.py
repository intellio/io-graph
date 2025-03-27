from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class ProtectionPolicyBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[ExchangeProtectionPolicy, OneDriveForBusinessProtectionPolicy, SharePointProtectionPolicy]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .exchange_protection_policy import ExchangeProtectionPolicy
from .one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy
from .share_point_protection_policy import SharePointProtectionPolicy

