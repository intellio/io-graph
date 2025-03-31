from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class AccessPackageAnswerString(BaseModel):
	answeredQuestion: Optional[Union[AccessPackageMultipleChoiceQuestion, AccessPackageTextInputQuestion]] = Field(alias="answeredQuestion", default=None,discriminator="odata_type", )
	displayValue: Optional[str] = Field(alias="displayValue", default=None,)
	odata_type: Literal["#microsoft.graph.accessPackageAnswerString"] = Field(alias="@odata.type", default="#microsoft.graph.accessPackageAnswerString")
	value: Optional[str] = Field(alias="value", default=None,)

from .access_package_multiple_choice_question import AccessPackageMultipleChoiceQuestion
from .access_package_text_input_question import AccessPackageTextInputQuestion
