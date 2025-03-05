from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ProvisioningStep(BaseModel):
	description: Optional[str] = Field(default=None,alias="description",)
	details: Optional[DetailsInfo] = Field(default=None,alias="details",)
	name: Optional[str] = Field(default=None,alias="name",)
	provisioningStepType: Optional[ProvisioningStepType] = Field(default=None,alias="provisioningStepType",)
	status: Optional[ProvisioningResult] = Field(default=None,alias="status",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .details_info import DetailsInfo
from .provisioning_step_type import ProvisioningStepType
from .provisioning_result import ProvisioningResult

