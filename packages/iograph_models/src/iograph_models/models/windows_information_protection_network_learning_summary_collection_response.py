from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsInformationProtectionNetworkLearningSummaryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[WindowsInformationProtectionNetworkLearningSummary]] = Field(default=None,alias="value",)

from .windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary

