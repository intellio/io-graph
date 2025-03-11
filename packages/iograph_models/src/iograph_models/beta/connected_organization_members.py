from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConnectedOrganizationMembers(BaseModel):
	isBackup: Optional[bool] = Field(alias="isBackup",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)


