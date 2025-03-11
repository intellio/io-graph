from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidWorkProfileNineWorkEasConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[AndroidWorkProfileNineWorkEasConfiguration]] = Field(alias="value",default=None,)

from .android_work_profile_nine_work_eas_configuration import AndroidWorkProfileNineWorkEasConfiguration

