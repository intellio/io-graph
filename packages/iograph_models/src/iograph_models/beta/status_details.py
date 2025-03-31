from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class StatusDetails(BaseModel):
	status: Optional[ProvisioningResult | str] = Field(alias="status", default=None,)
	odata_type: Literal["#microsoft.graph.statusDetails"] = Field(alias="@odata.type", default="#microsoft.graph.statusDetails")
	additionalDetails: Optional[str] = Field(alias="additionalDetails", default=None,)
	errorCategory: Optional[ProvisioningStatusErrorCategory | str] = Field(alias="errorCategory", default=None,)
	errorCode: Optional[str] = Field(alias="errorCode", default=None,)
	reason: Optional[str] = Field(alias="reason", default=None,)
	recommendedAction: Optional[str] = Field(alias="recommendedAction", default=None,)

from .provisioning_result import ProvisioningResult
from .provisioning_status_error_category import ProvisioningStatusErrorCategory
