from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsInformationProtectionStoreApp(BaseModel):
	denied: Optional[bool] = Field(default=None,alias="denied",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	productName: Optional[str] = Field(default=None,alias="productName",)
	publisherName: Optional[str] = Field(default=None,alias="publisherName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


