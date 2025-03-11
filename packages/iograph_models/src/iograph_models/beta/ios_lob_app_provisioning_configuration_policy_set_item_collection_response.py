from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IosLobAppProvisioningConfigurationPolicySetItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[IosLobAppProvisioningConfigurationPolicySetItem]] = Field(alias="value",default=None,)

from .ios_lob_app_provisioning_configuration_policy_set_item import IosLobAppProvisioningConfigurationPolicySetItem

