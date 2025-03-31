from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class IndustryDataAdministrativeUnitProvisioningFlow(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.industryData.administrativeUnitProvisioningFlow"] = Field(alias="@odata.type", default="#microsoft.graph.industryData.administrativeUnitProvisioningFlow")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	readinessStatus: Optional[IndustryDataReadinessStatus | str] = Field(alias="readinessStatus", default=None,)
	creationOptions: Optional[IndustryDataAdminUnitCreationOptions] = Field(alias="creationOptions", default=None,)

from .industry_data_readiness_status import IndustryDataReadinessStatus
from .industry_data_admin_unit_creation_options import IndustryDataAdminUnitCreationOptions
