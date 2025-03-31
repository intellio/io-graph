from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ServicePrincipalCreationConditionSet(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.servicePrincipalCreationConditionSet"] = Field(alias="@odata.type",)
	applicationIds: Optional[list[str]] = Field(alias="applicationIds", default=None,)
	applicationPublisherIds: Optional[list[str]] = Field(alias="applicationPublisherIds", default=None,)
	applicationsFromVerifiedPublisherOnly: Optional[bool] = Field(alias="applicationsFromVerifiedPublisherOnly", default=None,)
	applicationTenantIds: Optional[list[str]] = Field(alias="applicationTenantIds", default=None,)
	certifiedApplicationsOnly: Optional[bool] = Field(alias="certifiedApplicationsOnly", default=None,)

