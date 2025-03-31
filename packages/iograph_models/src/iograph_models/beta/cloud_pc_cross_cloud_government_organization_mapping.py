from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CloudPcCrossCloudGovernmentOrganizationMapping(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudPcCrossCloudGovernmentOrganizationMapping"] = Field(alias="@odata.type",)
	organizationIdsInUSGovCloud: Optional[list[str]] = Field(alias="organizationIdsInUSGovCloud", default=None,)

