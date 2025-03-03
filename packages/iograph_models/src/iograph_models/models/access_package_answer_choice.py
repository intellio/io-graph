from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessPackageAnswerChoice(BaseModel):
	actualValue: Optional[str] = Field(default=None,alias="actualValue",)
	localizations: Optional[list[AccessPackageLocalizedText]] = Field(default=None,alias="localizations",)
	text: Optional[str] = Field(default=None,alias="text",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .access_package_localized_text import AccessPackageLocalizedText

