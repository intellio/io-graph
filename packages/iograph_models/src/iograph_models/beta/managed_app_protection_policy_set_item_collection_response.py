from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedAppProtectionPolicySetItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ManagedAppProtectionPolicySetItem]] = Field(alias="value", default=None,)

from .managed_app_protection_policy_set_item import ManagedAppProtectionPolicySetItem

