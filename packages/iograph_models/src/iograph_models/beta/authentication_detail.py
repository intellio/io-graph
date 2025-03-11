from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationDetail(BaseModel):
	authenticationMethod: Optional[str] = Field(alias="authenticationMethod",default=None,)
	authenticationMethodDetail: Optional[str] = Field(alias="authenticationMethodDetail",default=None,)
	authenticationStepDateTime: Optional[datetime] = Field(alias="authenticationStepDateTime",default=None,)
	authenticationStepRequirement: Optional[str] = Field(alias="authenticationStepRequirement",default=None,)
	authenticationStepResultDetail: Optional[str] = Field(alias="authenticationStepResultDetail",default=None,)
	succeeded: Optional[bool] = Field(alias="succeeded",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


