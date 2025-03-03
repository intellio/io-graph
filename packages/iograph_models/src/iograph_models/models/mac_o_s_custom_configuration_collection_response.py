from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MacOSCustomConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[MacOSCustomConfiguration]] = Field(default=None,alias="value",)

from .mac_o_s_custom_configuration import MacOSCustomConfiguration

