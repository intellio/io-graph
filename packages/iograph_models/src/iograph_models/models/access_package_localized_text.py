from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessPackageLocalizedText(BaseModel):
	languageCode: Optional[str] = Field(default=None,alias="languageCode",)
	text: Optional[str] = Field(default=None,alias="text",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


