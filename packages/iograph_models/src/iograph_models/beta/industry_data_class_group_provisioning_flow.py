from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class IndustryDataClassGroupProvisioningFlow(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.industryData.classGroupProvisioningFlow"] = Field(alias="@odata.type", default="#microsoft.graph.industryData.classGroupProvisioningFlow")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	readinessStatus: Optional[IndustryDataReadinessStatus | str] = Field(alias="readinessStatus", default=None,)
	configuration: Optional[IndustryDataClassGroupConfiguration] = Field(alias="configuration", default=None,)

from .industry_data_readiness_status import IndustryDataReadinessStatus
from .industry_data_class_group_configuration import IndustryDataClassGroupConfiguration
