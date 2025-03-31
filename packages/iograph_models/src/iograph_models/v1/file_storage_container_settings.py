from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class FileStorageContainerSettings(BaseModel):
	isItemVersioningEnabled: Optional[bool] = Field(alias="isItemVersioningEnabled", default=None,)
	isOcrEnabled: Optional[bool] = Field(alias="isOcrEnabled", default=None,)
	itemMajorVersionLimit: Optional[int] = Field(alias="itemMajorVersionLimit", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

