from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class IndustryDataUserProvisioningFlow(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.industryData.userProvisioningFlow"] = Field(alias="@odata.type", default="#microsoft.graph.industryData.userProvisioningFlow")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	readinessStatus: Optional[IndustryDataReadinessStatus | str] = Field(alias="readinessStatus", default=None,)
	createUnmatchedUsers: Optional[bool] = Field(alias="createUnmatchedUsers", default=None,)
	creationOptions: Optional[IndustryDataUserCreationOptions] = Field(alias="creationOptions", default=None,)
	managementOptions: Optional[IndustryDataUserManagementOptions] = Field(alias="managementOptions", default=None,)

from .industry_data_readiness_status import IndustryDataReadinessStatus
from .industry_data_user_creation_options import IndustryDataUserCreationOptions
from .industry_data_user_management_options import IndustryDataUserManagementOptions
