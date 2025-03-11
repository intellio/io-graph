from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Windows10EasEmailProfileConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[Windows10EasEmailProfileConfiguration]] = Field(alias="value",default=None,)

from .windows10_eas_email_profile_configuration import Windows10EasEmailProfileConfiguration

