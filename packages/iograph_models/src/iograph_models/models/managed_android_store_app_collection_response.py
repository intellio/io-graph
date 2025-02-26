from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedAndroidStoreAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ManagedAndroidStoreApp] = Field(alias="value",)

from .managed_android_store_app import ManagedAndroidStoreApp

