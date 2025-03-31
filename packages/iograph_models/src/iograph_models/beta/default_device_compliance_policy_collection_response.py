from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DefaultDeviceCompliancePolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[DefaultDeviceCompliancePolicy]] = Field(alias="value", default=None,)

from .default_device_compliance_policy import DefaultDeviceCompliancePolicy
