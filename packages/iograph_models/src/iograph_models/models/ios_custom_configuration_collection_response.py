from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosCustomConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[IosCustomConfiguration] = Field(alias="value",)

from .ios_custom_configuration import IosCustomConfiguration

