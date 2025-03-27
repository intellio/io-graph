from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ProvisioningErrorInfo(BaseModel):
	additionalDetails: Optional[str] = Field(alias="additionalDetails", default=None,)
	errorCategory: Optional[ProvisioningStatusErrorCategory | str] = Field(alias="errorCategory", default=None,)
	errorCode: Optional[str] = Field(alias="errorCode", default=None,)
	reason: Optional[str] = Field(alias="reason", default=None,)
	recommendedAction: Optional[str] = Field(alias="recommendedAction", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .provisioning_status_error_category import ProvisioningStatusErrorCategory

