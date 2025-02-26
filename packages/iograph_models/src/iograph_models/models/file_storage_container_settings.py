from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class FileStorageContainerSettings(BaseModel):
	isItemVersioningEnabled: Optional[bool] = Field(default=None,alias="isItemVersioningEnabled",)
	isOcrEnabled: Optional[bool] = Field(default=None,alias="isOcrEnabled",)
	itemMajorVersionLimit: Optional[int] = Field(default=None,alias="itemMajorVersionLimit",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


