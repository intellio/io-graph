from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageTextInputQuestion(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	isAnswerEditable: Optional[bool] = Field(alias="isAnswerEditable",default=None,)
	isRequired: Optional[bool] = Field(alias="isRequired",default=None,)
	sequence: Optional[int] = Field(alias="sequence",default=None,)
	text: Optional[AccessPackageLocalizedContent] = Field(alias="text",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	isSingleLineQuestion: Optional[bool] = Field(alias="isSingleLineQuestion",default=None,)
	regexPattern: Optional[str] = Field(alias="regexPattern",default=None,)

from .access_package_localized_content import AccessPackageLocalizedContent

