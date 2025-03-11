from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EasEmailProfileConfigurationBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[EasEmailProfileConfigurationBase]]] = Field(alias="value",default=None,)

from .eas_email_profile_configuration_base import EasEmailProfileConfigurationBase

