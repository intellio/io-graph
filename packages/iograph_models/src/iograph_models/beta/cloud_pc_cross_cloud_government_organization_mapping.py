from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcCrossCloudGovernmentOrganizationMapping(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	organizationIdsInUSGovCloud: Optional[list[str]] = Field(alias="organizationIdsInUSGovCloud", default=None,)


