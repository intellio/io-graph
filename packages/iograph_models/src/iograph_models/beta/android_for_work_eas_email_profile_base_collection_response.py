from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidForWorkEasEmailProfileBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[AndroidForWorkEasEmailProfileBase]]] = Field(alias="value",default=None,)

from .android_for_work_eas_email_profile_base import AndroidForWorkEasEmailProfileBase

