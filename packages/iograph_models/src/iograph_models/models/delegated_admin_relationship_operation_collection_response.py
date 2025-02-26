from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DelegatedAdminRelationshipOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[DelegatedAdminRelationshipOperation] = Field(alias="value",)

from .delegated_admin_relationship_operation import DelegatedAdminRelationshipOperation

