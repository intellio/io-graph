from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppsInstallationOptionsForMac(BaseModel):
	isMicrosoft365AppsEnabled: Optional[bool] = Field(default=None,alias="isMicrosoft365AppsEnabled",)
	isSkypeForBusinessEnabled: Optional[bool] = Field(default=None,alias="isSkypeForBusinessEnabled",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


