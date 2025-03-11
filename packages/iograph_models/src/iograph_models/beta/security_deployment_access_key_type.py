from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityDeploymentAccessKeyType(BaseModel):
	deploymentAccessKey: Optional[str] = Field(alias="deploymentAccessKey",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


