from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataAdministrativeUnitProvisioningFlowCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[IndustryDataAdministrativeUnitProvisioningFlow]] = Field(alias="value",default=None,)

from .industry_data_administrative_unit_provisioning_flow import IndustryDataAdministrativeUnitProvisioningFlow

