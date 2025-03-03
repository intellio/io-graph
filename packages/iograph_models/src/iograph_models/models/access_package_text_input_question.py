from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessPackageTextInputQuestion(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	isAnswerEditable: Optional[bool] = Field(default=None,alias="isAnswerEditable",)
	isRequired: Optional[bool] = Field(default=None,alias="isRequired",)
	localizations: Optional[list[AccessPackageLocalizedText]] = Field(default=None,alias="localizations",)
	sequence: Optional[int] = Field(default=None,alias="sequence",)
	text: Optional[str] = Field(default=None,alias="text",)
	isSingleLineQuestion: Optional[bool] = Field(default=None,alias="isSingleLineQuestion",)
	regexPattern: Optional[str] = Field(default=None,alias="regexPattern",)

from .access_package_localized_text import AccessPackageLocalizedText

