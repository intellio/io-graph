from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppsInstallationOptionsForWindows(BaseModel):
	isMicrosoft365AppsEnabled: Optional[bool] = Field(alias="isMicrosoft365AppsEnabled",default=None,)
	isProjectEnabled: Optional[bool] = Field(alias="isProjectEnabled",default=None,)
	isSkypeForBusinessEnabled: Optional[bool] = Field(alias="isSkypeForBusinessEnabled",default=None,)
	isVisioEnabled: Optional[bool] = Field(alias="isVisioEnabled",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


