from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DelegatedPermissionClassificationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[DelegatedPermissionClassification]] = Field(alias="value",default=None,)

from .delegated_permission_classification import DelegatedPermissionClassification

