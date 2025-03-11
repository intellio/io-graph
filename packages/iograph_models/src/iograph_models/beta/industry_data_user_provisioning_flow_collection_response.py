from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataUserProvisioningFlowCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[IndustryDataUserProvisioningFlow]] = Field(alias="value",default=None,)

from .industry_data_user_provisioning_flow import IndustryDataUserProvisioningFlow

