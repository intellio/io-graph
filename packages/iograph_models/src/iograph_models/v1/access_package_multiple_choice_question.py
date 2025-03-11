from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageMultipleChoiceQuestion(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	isAnswerEditable: Optional[bool] = Field(alias="isAnswerEditable",default=None,)
	isRequired: Optional[bool] = Field(alias="isRequired",default=None,)
	localizations: Optional[list[AccessPackageLocalizedText]] = Field(alias="localizations",default=None,)
	sequence: Optional[int] = Field(alias="sequence",default=None,)
	text: Optional[str] = Field(alias="text",default=None,)
	choices: Optional[list[AccessPackageAnswerChoice]] = Field(alias="choices",default=None,)
	isMultipleSelectionAllowed: Optional[bool] = Field(alias="isMultipleSelectionAllowed",default=None,)

from .access_package_localized_text import AccessPackageLocalizedText
from .access_package_answer_choice import AccessPackageAnswerChoice

