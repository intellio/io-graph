from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ProfileCardAnnotation(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	localizations: Optional[list[DisplayNameLocalization]] = Field(alias="localizations", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .display_name_localization import DisplayNameLocalization
