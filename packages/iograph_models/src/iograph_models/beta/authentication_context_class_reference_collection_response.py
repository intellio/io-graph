from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationContextClassReferenceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AuthenticationContextClassReference]] = Field(alias="value", default=None,)

from .authentication_context_class_reference import AuthenticationContextClassReference
