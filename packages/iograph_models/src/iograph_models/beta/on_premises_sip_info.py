from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnPremisesSipInfo(BaseModel):
	isSipEnabled: Optional[bool] = Field(alias="isSipEnabled",default=None,)
	sipDeploymentLocation: Optional[str] = Field(alias="sipDeploymentLocation",default=None,)
	sipPrimaryAddress: Optional[str] = Field(alias="sipPrimaryAddress",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


