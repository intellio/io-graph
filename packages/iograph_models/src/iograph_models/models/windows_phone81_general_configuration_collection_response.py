from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsPhone81GeneralConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[WindowsPhone81GeneralConfiguration] = Field(alias="value",)

from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration

