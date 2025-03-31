from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityDepartmentTemplateCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecurityDepartmentTemplate]] = Field(alias="value", default=None,)

from .security_department_template import SecurityDepartmentTemplate
