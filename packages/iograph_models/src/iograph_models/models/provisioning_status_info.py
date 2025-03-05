from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ProvisioningStatusInfo(BaseModel):
	errorInformation: Optional[ProvisioningErrorInfo] = Field(default=None,alias="errorInformation",)
	status: Optional[ProvisioningResult] = Field(default=None,alias="status",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .provisioning_error_info import ProvisioningErrorInfo
from .provisioning_result import ProvisioningResult

