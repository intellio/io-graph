from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TargetedManagedAppConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[TargetedManagedAppConfiguration] = Field(alias="value",)

from .targeted_managed_app_configuration import TargetedManagedAppConfiguration

