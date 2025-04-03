from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WindowsInformationProtectionAppLearningSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsInformationProtectionAppLearningSummary"] = Field(alias="@odata.type", default="#microsoft.graph.windowsInformationProtectionAppLearningSummary")
	applicationName: Optional[str] = Field(alias="applicationName", default=None,)
	applicationType: Optional[ApplicationType | str] = Field(alias="applicationType", default=None,)
	deviceCount: Optional[int] = Field(alias="deviceCount", default=None,)

from .application_type import ApplicationType
