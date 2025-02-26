from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AndroidManagedAppRegistrationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AndroidManagedAppRegistration] = Field(alias="value",)

from .android_managed_app_registration import AndroidManagedAppRegistration

