from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OnPremisesProvisioningErrorCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[OnPremisesProvisioningError]] = Field(default=None,alias="value",)

from .on_premises_provisioning_error import OnPremisesProvisioningError

