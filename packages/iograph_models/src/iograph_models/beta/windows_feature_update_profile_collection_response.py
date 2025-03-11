from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsFeatureUpdateProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[WindowsFeatureUpdateProfile]] = Field(alias="value",default=None,)

from .windows_feature_update_profile import WindowsFeatureUpdateProfile

