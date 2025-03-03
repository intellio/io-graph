from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ColumnValidation(BaseModel):
	defaultLanguage: Optional[str] = Field(default=None,alias="defaultLanguage",)
	descriptions: Optional[list[DisplayNameLocalization]] = Field(default=None,alias="descriptions",)
	formula: Optional[str] = Field(default=None,alias="formula",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .display_name_localization import DisplayNameLocalization

