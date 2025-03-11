from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessClientApplications(BaseModel):
	excludeServicePrincipals: Optional[list[str]] = Field(alias="excludeServicePrincipals",default=None,)
	includeServicePrincipals: Optional[list[str]] = Field(alias="includeServicePrincipals",default=None,)
	servicePrincipalFilter: Optional[ConditionalAccessFilter] = Field(alias="servicePrincipalFilter",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .conditional_access_filter import ConditionalAccessFilter

