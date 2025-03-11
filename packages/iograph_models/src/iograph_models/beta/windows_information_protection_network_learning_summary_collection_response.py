from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsInformationProtectionNetworkLearningSummaryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[WindowsInformationProtectionNetworkLearningSummary]] = Field(alias="value",default=None,)

from .windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary

