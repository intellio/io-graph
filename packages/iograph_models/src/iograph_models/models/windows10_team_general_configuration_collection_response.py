from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Windows10TeamGeneralConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[Windows10TeamGeneralConfiguration] = Field(alias="value",)

from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration

