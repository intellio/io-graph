from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class FileStorageContainerCustomPropertyValue(BaseModel):
	isSearchable: Optional[bool] = Field(default=None,alias="isSearchable",)
	value: Optional[str] = Field(default=None,alias="value",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


