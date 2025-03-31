from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ColumnValidation(BaseModel):
	defaultLanguage: Optional[str] = Field(alias="defaultLanguage", default=None,)
	descriptions: Optional[list[DisplayNameLocalization]] = Field(alias="descriptions", default=None,)
	formula: Optional[str] = Field(alias="formula", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .display_name_localization import DisplayNameLocalization
