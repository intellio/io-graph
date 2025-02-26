from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessPackageResourceAttributeQuestion(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	question: Optional[AccessPackageQuestion] = Field(default=None,alias="question",)

from .access_package_question import AccessPackageQuestion

