from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LoginPageBrandingVisualElement(BaseModel):
	customText: Optional[str] = Field(alias="customText", default=None,)
	customUrl: Optional[str] = Field(alias="customUrl", default=None,)
	isHidden: Optional[bool] = Field(alias="isHidden", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


