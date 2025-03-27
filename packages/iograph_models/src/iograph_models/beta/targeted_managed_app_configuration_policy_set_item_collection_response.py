from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TargetedManagedAppConfigurationPolicySetItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[TargetedManagedAppConfigurationPolicySetItem]] = Field(alias="value", default=None,)

from .targeted_managed_app_configuration_policy_set_item import TargetedManagedAppConfigurationPolicySetItem

