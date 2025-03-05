from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsInformationProtectionDesktopApp(BaseModel):
	denied: Optional[bool] = Field(alias="denied",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	productName: Optional[str] = Field(alias="productName",default=None,)
	publisherName: Optional[str] = Field(alias="publisherName",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	binaryName: Optional[str] = Field(alias="binaryName",default=None,)
	binaryVersionHigh: Optional[str] = Field(alias="binaryVersionHigh",default=None,)
	binaryVersionLow: Optional[str] = Field(alias="binaryVersionLow",default=None,)


