from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageAnswerChoice(BaseModel):
	actualValue: Optional[str] = Field(alias="actualValue", default=None,)
	localizations: Optional[list[AccessPackageLocalizedText]] = Field(alias="localizations", default=None,)
	text: Optional[str] = Field(alias="text", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .access_package_localized_text import AccessPackageLocalizedText

