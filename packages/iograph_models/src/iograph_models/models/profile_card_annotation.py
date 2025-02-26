from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ProfileCardAnnotation(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	localizations: list[DisplayNameLocalization] = Field(alias="localizations",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .display_name_localization import DisplayNameLocalization

