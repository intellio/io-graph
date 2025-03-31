from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class AccessPackageResourceAttributeQuestion(BaseModel):
	odata_type: Literal["#microsoft.graph.accessPackageResourceAttributeQuestion"] = Field(alias="@odata.type", default="#microsoft.graph.accessPackageResourceAttributeQuestion")
	question: Optional[Union[AccessPackageMultipleChoiceQuestion, AccessPackageTextInputQuestion]] = Field(alias="question", default=None,discriminator="odata_type", )

from .access_package_multiple_choice_question import AccessPackageMultipleChoiceQuestion
from .access_package_text_input_question import AccessPackageTextInputQuestion
