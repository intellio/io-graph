from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EducationItemBody(BaseModel):
	content: Optional[str] = Field(alias="content", default=None,)
	contentType: Optional[BodyType | str] = Field(alias="contentType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .body_type import BodyType
