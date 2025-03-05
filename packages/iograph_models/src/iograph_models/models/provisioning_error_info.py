from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ProvisioningErrorInfo(BaseModel):
	additionalDetails: Optional[str] = Field(default=None,alias="additionalDetails",)
	errorCategory: Optional[ProvisioningStatusErrorCategory] = Field(default=None,alias="errorCategory",)
	errorCode: Optional[str] = Field(default=None,alias="errorCode",)
	reason: Optional[str] = Field(default=None,alias="reason",)
	recommendedAction: Optional[str] = Field(default=None,alias="recommendedAction",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .provisioning_status_error_category import ProvisioningStatusErrorCategory

