from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageLocalizedContent(BaseModel):
	defaultText: Optional[str] = Field(alias="defaultText",default=None,)
	localizedTexts: Optional[list[AccessPackageLocalizedText]] = Field(alias="localizedTexts",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .access_package_localized_text import AccessPackageLocalizedText

