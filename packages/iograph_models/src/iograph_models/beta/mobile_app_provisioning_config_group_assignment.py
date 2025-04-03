from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class MobileAppProvisioningConfigGroupAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.mobileAppProvisioningConfigGroupAssignment"] = Field(alias="@odata.type", default="#microsoft.graph.mobileAppProvisioningConfigGroupAssignment")
	targetGroupId: Optional[str] = Field(alias="targetGroupId", default=None,)

