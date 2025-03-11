from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ActiveUsersMetric(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appId: Optional[str] = Field(alias="appId",default=None,)
	appName: Optional[str] = Field(alias="appName",default=None,)
	count: Optional[int] = Field(alias="count",default=None,)
	country: Optional[str] = Field(alias="country",default=None,)
	factDate: Optional[str] = Field(alias="factDate",default=None,)
	language: Optional[str] = Field(alias="language",default=None,)
	os: Optional[str] = Field(alias="os",default=None,)


