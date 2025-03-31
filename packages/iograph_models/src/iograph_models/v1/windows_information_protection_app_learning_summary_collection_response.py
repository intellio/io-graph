from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsInformationProtectionAppLearningSummaryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[WindowsInformationProtectionAppLearningSummary]] = Field(alias="value", default=None,)

from .windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
