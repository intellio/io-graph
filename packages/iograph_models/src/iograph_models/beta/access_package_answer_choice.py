from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessPackageAnswerChoice(BaseModel):
	actualValue: Optional[str] = Field(alias="actualValue", default=None,)
	displayValue: Optional[AccessPackageLocalizedContent] = Field(alias="displayValue", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .access_package_localized_content import AccessPackageLocalizedContent
