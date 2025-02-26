from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessPackageAnswerString(BaseModel):
	displayValue: Optional[str] = Field(default=None,alias="displayValue",)
	answeredQuestion: Optional[AccessPackageQuestion] = Field(default=None,alias="answeredQuestion",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	value: Optional[str] = Field(default=None,alias="value",)

from .access_package_question import AccessPackageQuestion

