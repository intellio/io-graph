from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class InformationProtectionLabelCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[InformationProtectionLabel]] = Field(alias="value", default=None,)

from .information_protection_label import InformationProtectionLabel
