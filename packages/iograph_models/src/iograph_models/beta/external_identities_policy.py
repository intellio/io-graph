from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ExternalIdentitiesPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.externalIdentitiesPolicy"] = Field(alias="@odata.type", default="#microsoft.graph.externalIdentitiesPolicy")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	allowDeletedIdentitiesDataRemoval: Optional[bool] = Field(alias="allowDeletedIdentitiesDataRemoval", default=None,)
	allowExternalIdentitiesToLeave: Optional[bool] = Field(alias="allowExternalIdentitiesToLeave", default=None,)

