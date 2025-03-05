from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LoginPageLayoutConfiguration(BaseModel):
	isFooterShown: Optional[bool] = Field(default=None,alias="isFooterShown",)
	isHeaderShown: Optional[bool] = Field(default=None,alias="isHeaderShown",)
	layoutTemplateType: Optional[LayoutTemplateType] = Field(default=None,alias="layoutTemplateType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .layout_template_type import LayoutTemplateType

