from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ProvisioningStatusInfo(BaseModel):
	errorInformation: Optional[ProvisioningErrorInfo] = Field(alias="errorInformation", default=None,)
	status: Optional[ProvisioningResult | str] = Field(alias="status", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .provisioning_error_info import ProvisioningErrorInfo
from .provisioning_result import ProvisioningResult

