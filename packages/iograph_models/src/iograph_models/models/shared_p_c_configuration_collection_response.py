from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SharedPCConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SharedPCConfiguration] = Field(alias="value",)

from .shared_p_c_configuration import SharedPCConfiguration

