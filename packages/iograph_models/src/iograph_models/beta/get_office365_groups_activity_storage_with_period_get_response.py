from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_office365_groups_activity_storage_with_periodGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Office365GroupsActivityStorage]] = Field(alias="value", default=None,)

from .office365_groups_activity_storage import Office365GroupsActivityStorage

