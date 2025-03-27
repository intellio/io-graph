from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsManagedTenantExecutionError(BaseModel):
	error: Optional[str] = Field(alias="error", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.managedTenantExecutionError"] = Field(alias="@odata.type", default="#microsoft.graph.managedTenants.managedTenantExecutionError")
	errorDetails: Optional[str] = Field(alias="errorDetails", default=None,)
	nodeId: Optional[int] = Field(alias="nodeId", default=None,)
	rawToken: Optional[str] = Field(alias="rawToken", default=None,)
	statementIndex: Optional[int] = Field(alias="statementIndex", default=None,)


