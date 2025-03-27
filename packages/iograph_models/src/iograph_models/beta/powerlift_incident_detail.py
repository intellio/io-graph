from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PowerliftIncidentDetail(BaseModel):
	applicationName: Optional[str] = Field(alias="applicationName", default=None,)
	clientApplicationVersion: Optional[str] = Field(alias="clientApplicationVersion", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	easyId: Optional[str] = Field(alias="easyId", default=None,)
	fileNames: Optional[list[str]] = Field(alias="fileNames", default=None,)
	locale: Optional[str] = Field(alias="locale", default=None,)
	platformDisplayName: Optional[str] = Field(alias="platformDisplayName", default=None,)
	powerliftId: Optional[str] = Field(alias="powerliftId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


