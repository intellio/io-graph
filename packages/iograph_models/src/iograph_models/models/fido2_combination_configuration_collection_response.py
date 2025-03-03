from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Fido2CombinationConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[Fido2CombinationConfiguration]] = Field(default=None,alias="value",)

from .fido2_combination_configuration import Fido2CombinationConfiguration

