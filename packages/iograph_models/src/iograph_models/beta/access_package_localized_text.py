from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageLocalizedText(BaseModel):
	languageCode: Optional[str] = Field(alias="languageCode", default=None,)
	text: Optional[str] = Field(alias="text", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


