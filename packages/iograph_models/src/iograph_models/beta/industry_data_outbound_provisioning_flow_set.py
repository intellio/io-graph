from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataOutboundProvisioningFlowSet(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	filter: SerializeAsAny[Optional[IndustryDataFilter]] = Field(alias="filter",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	provisioningFlows: SerializeAsAny[Optional[list[IndustryDataProvisioningFlow]]] = Field(alias="provisioningFlows",default=None,)

from .industry_data_filter import IndustryDataFilter
from .industry_data_provisioning_flow import IndustryDataProvisioningFlow

