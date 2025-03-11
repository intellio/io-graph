from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsManagedTenantExecutionError(BaseModel):
	error: Optional[str] = Field(alias="error",default=None,)
	tenantId: Optional[str] = Field(alias="tenantId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	errorDetails: Optional[str] = Field(alias="errorDetails",default=None,)
	nodeId: Optional[int] = Field(alias="nodeId",default=None,)
	rawToken: Optional[str] = Field(alias="rawToken",default=None,)
	statementIndex: Optional[int] = Field(alias="statementIndex",default=None,)


