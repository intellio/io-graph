from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RestrictedAppsViolationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[RestrictedAppsViolation]] = Field(alias="value", default=None,)

from .restricted_apps_violation import RestrictedAppsViolation
