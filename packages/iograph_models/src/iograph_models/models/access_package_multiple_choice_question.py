from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessPackageMultipleChoiceQuestion(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	isAnswerEditable: Optional[bool] = Field(default=None,alias="isAnswerEditable",)
	isRequired: Optional[bool] = Field(default=None,alias="isRequired",)
	localizations: list[AccessPackageLocalizedText] = Field(alias="localizations",)
	sequence: Optional[int] = Field(default=None,alias="sequence",)
	text: Optional[str] = Field(default=None,alias="text",)
	choices: list[AccessPackageAnswerChoice] = Field(alias="choices",)
	isMultipleSelectionAllowed: Optional[bool] = Field(default=None,alias="isMultipleSelectionAllowed",)

from .access_package_localized_text import AccessPackageLocalizedText
from .access_package_answer_choice import AccessPackageAnswerChoice

