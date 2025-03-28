from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MicrosoftApplicationDataAccessSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	disabledForGroup: Optional[str] = Field(alias="disabledForGroup", default=None,)
	isEnabledForAllMicrosoftApplications: Optional[bool] = Field(alias="isEnabledForAllMicrosoftApplications", default=None,)


