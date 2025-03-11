from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalIdentitiesPolicy(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	allowDeletedIdentitiesDataRemoval: Optional[bool] = Field(alias="allowDeletedIdentitiesDataRemoval",default=None,)
	allowExternalIdentitiesToLeave: Optional[bool] = Field(alias="allowExternalIdentitiesToLeave",default=None,)


