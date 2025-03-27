from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TargetedManagedAppConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[TargetedManagedAppConfiguration]] = Field(alias="value", default=None,)

from .targeted_managed_app_configuration import TargetedManagedAppConfiguration

