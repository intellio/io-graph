from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ServicePrincipalCreationConditionSetCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[ServicePrincipalCreationConditionSet]] = Field(alias="value",default=None,)

from .service_principal_creation_condition_set import ServicePrincipalCreationConditionSet

