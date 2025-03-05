from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidWorkProfileCustomConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[AndroidWorkProfileCustomConfiguration]] = Field(default=None,alias="value",)

from .android_work_profile_custom_configuration import AndroidWorkProfileCustomConfiguration

