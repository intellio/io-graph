from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LoginPageLayoutConfiguration(BaseModel):
	isFooterShown: Optional[bool] = Field(alias="isFooterShown",default=None,)
	isHeaderShown: Optional[bool] = Field(alias="isHeaderShown",default=None,)
	layoutTemplateType: Optional[LayoutTemplateType | str] = Field(alias="layoutTemplateType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .layout_template_type import LayoutTemplateType

