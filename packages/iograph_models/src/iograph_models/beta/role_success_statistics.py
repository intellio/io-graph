from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RoleSuccessStatistics(BaseModel):
	permanentFail: Optional[int] = Field(alias="permanentFail", default=None,)
	permanentSuccess: Optional[int] = Field(alias="permanentSuccess", default=None,)
	removeFail: Optional[int] = Field(alias="removeFail", default=None,)
	removeSuccess: Optional[int] = Field(alias="removeSuccess", default=None,)
	roleId: Optional[str] = Field(alias="roleId", default=None,)
	roleName: Optional[str] = Field(alias="roleName", default=None,)
	temporaryFail: Optional[int] = Field(alias="temporaryFail", default=None,)
	temporarySuccess: Optional[int] = Field(alias="temporarySuccess", default=None,)
	unknownFail: Optional[int] = Field(alias="unknownFail", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


