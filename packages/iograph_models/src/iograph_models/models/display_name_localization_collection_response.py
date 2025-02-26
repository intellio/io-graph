from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DisplayNameLocalizationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[DisplayNameLocalization] = Field(alias="value",)

from .display_name_localization import DisplayNameLocalization

