from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ServiceProvisioningErrorCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ServiceProvisioningError] = Field(alias="value",)

from .service_provisioning_error import ServiceProvisioningError

