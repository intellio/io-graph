from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class AccessPackageQuestionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AccessPackageMultipleChoiceQuestion, AccessPackageTextInputQuestion],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .access_package_multiple_choice_question import AccessPackageMultipleChoiceQuestion
from .access_package_text_input_question import AccessPackageTextInputQuestion
