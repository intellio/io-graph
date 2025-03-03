from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsPhone81GeneralConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[WindowsPhone81GeneralConfiguration]] = Field(default=None,alias="value",)

from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration

