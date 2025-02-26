from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserConsentRequestCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[UserConsentRequest] = Field(alias="value",)

from .user_consent_request import UserConsentRequest

