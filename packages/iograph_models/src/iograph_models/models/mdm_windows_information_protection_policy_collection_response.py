from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MdmWindowsInformationProtectionPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[MdmWindowsInformationProtectionPolicy] = Field(alias="value",)

from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy

