from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TargetedManagedAppProtectionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[TargetedManagedAppProtection]]] = Field(alias="value",default=None,)

from .targeted_managed_app_protection import TargetedManagedAppProtection

