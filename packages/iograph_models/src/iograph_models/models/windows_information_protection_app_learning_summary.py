from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsInformationProtectionAppLearningSummary(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	applicationName: Optional[str] = Field(default=None,alias="applicationName",)
	applicationType: Optional[ApplicationType] = Field(default=None,alias="applicationType",)
	deviceCount: Optional[int] = Field(default=None,alias="deviceCount",)

from .application_type import ApplicationType

