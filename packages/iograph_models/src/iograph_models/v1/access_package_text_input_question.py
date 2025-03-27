from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageTextInputQuestion(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.accessPackageTextInputQuestion"] = Field(alias="@odata.type", default="#microsoft.graph.accessPackageTextInputQuestion")
	isAnswerEditable: Optional[bool] = Field(alias="isAnswerEditable", default=None,)
	isRequired: Optional[bool] = Field(alias="isRequired", default=None,)
	localizations: Optional[list[AccessPackageLocalizedText]] = Field(alias="localizations", default=None,)
	sequence: Optional[int] = Field(alias="sequence", default=None,)
	text: Optional[str] = Field(alias="text", default=None,)
	isSingleLineQuestion: Optional[bool] = Field(alias="isSingleLineQuestion", default=None,)
	regexPattern: Optional[str] = Field(alias="regexPattern", default=None,)

from .access_package_localized_text import AccessPackageLocalizedText

