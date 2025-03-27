from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnPremisesCurrentExportData(BaseModel):
	clientMachineName: Optional[str] = Field(alias="clientMachineName", default=None,)
	pendingObjectsAddition: Optional[int] = Field(alias="pendingObjectsAddition", default=None,)
	pendingObjectsDeletion: Optional[int] = Field(alias="pendingObjectsDeletion", default=None,)
	pendingObjectsUpdate: Optional[int] = Field(alias="pendingObjectsUpdate", default=None,)
	serviceAccount: Optional[str] = Field(alias="serviceAccount", default=None,)
	successfulLinksProvisioningCount: Optional[int] = Field(alias="successfulLinksProvisioningCount", default=None,)
	successfulObjectsProvisioningCount: Optional[int] = Field(alias="successfulObjectsProvisioningCount", default=None,)
	totalConnectorSpaceObjects: Optional[int] = Field(alias="totalConnectorSpaceObjects", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


