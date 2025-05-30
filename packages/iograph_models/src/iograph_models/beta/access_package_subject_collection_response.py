from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessPackageSubjectCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AccessPackageSubject]] = Field(alias="value", default=None,)

from .access_package_subject import AccessPackageSubject
