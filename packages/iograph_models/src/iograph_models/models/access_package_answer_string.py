from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageAnswerString(BaseModel):
	displayValue: Optional[str] = Field(alias="displayValue",default=None,)
	answeredQuestion: SerializeAsAny[Optional[AccessPackageQuestion]] = Field(alias="answeredQuestion",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	value: Optional[str] = Field(alias="value",default=None,)

from .access_package_question import AccessPackageQuestion

