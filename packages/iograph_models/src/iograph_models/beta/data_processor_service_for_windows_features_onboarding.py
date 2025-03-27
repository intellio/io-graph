from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DataProcessorServiceForWindowsFeaturesOnboarding(BaseModel):
	areDataProcessorServiceForWindowsFeaturesEnabled: Optional[bool] = Field(alias="areDataProcessorServiceForWindowsFeaturesEnabled", default=None,)
	hasValidWindowsLicense: Optional[bool] = Field(alias="hasValidWindowsLicense", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


