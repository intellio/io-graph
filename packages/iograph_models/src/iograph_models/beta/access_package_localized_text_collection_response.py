from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessPackageLocalizedTextCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AccessPackageLocalizedText]] = Field(alias="value", default=None,)

from .access_package_localized_text import AccessPackageLocalizedText
