from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageMultipleChoiceQuestion(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	isAnswerEditable: Optional[bool] = Field(alias="isAnswerEditable", default=None,)
	isRequired: Optional[bool] = Field(alias="isRequired", default=None,)
	sequence: Optional[int] = Field(alias="sequence", default=None,)
	text: Optional[AccessPackageLocalizedContent] = Field(alias="text", default=None,)
	odata_type: Literal["#microsoft.graph.accessPackageMultipleChoiceQuestion"] = Field(alias="@odata.type", default="#microsoft.graph.accessPackageMultipleChoiceQuestion")
	allowsMultipleSelection: Optional[bool] = Field(alias="allowsMultipleSelection", default=None,)
	choices: Optional[list[AccessPackageAnswerChoice]] = Field(alias="choices", default=None,)

from .access_package_localized_content import AccessPackageLocalizedContent
from .access_package_answer_choice import AccessPackageAnswerChoice

