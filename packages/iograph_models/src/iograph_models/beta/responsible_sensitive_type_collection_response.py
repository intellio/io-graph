from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ResponsibleSensitiveTypeCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ResponsibleSensitiveType]] = Field(alias="value", default=None,)

from .responsible_sensitive_type import ResponsibleSensitiveType
