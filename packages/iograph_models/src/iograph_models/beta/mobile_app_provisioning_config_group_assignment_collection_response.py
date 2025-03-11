from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MobileAppProvisioningConfigGroupAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[MobileAppProvisioningConfigGroupAssignment]] = Field(alias="value",default=None,)

from .mobile_app_provisioning_config_group_assignment import MobileAppProvisioningConfigGroupAssignment

