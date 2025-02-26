from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessPackageQuestionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AccessPackageQuestion] = Field(alias="value",)

from .access_package_question import AccessPackageQuestion

