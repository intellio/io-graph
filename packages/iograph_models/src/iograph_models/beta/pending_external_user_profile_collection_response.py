from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PendingExternalUserProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[PendingExternalUserProfile]] = Field(alias="value",default=None,)

from .pending_external_user_profile import PendingExternalUserProfile

