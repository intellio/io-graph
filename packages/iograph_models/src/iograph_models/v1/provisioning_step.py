from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ProvisioningStep(BaseModel):
	description: Optional[str] = Field(alias="description", default=None,)
	details: Optional[DetailsInfo] = Field(alias="details", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	provisioningStepType: Optional[ProvisioningStepType | str] = Field(alias="provisioningStepType", default=None,)
	status: Optional[ProvisioningResult | str] = Field(alias="status", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .details_info import DetailsInfo
from .provisioning_step_type import ProvisioningStepType
from .provisioning_result import ProvisioningResult

