from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsInformationProtectionAppLearningSummary(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	applicationName: Optional[str] = Field(alias="applicationName",default=None,)
	applicationType: Optional[ApplicationType | str] = Field(alias="applicationType",default=None,)
	deviceCount: Optional[int] = Field(alias="deviceCount",default=None,)

from .application_type import ApplicationType

