from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppsInstallationOptionsForWindows(BaseModel):
	isMicrosoft365AppsEnabled: Optional[bool] = Field(default=None,alias="isMicrosoft365AppsEnabled",)
	isProjectEnabled: Optional[bool] = Field(default=None,alias="isProjectEnabled",)
	isSkypeForBusinessEnabled: Optional[bool] = Field(default=None,alias="isSkypeForBusinessEnabled",)
	isVisioEnabled: Optional[bool] = Field(default=None,alias="isVisioEnabled",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


