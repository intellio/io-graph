from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Windows81GeneralConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[Windows81GeneralConfiguration] = Field(alias="value",)

from .windows81_general_configuration import Windows81GeneralConfiguration

