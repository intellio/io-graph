from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataOutboundProvisioningFlowSet(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	filter: Optional[Union[IndustryDataBasicFilter]] = Field(alias="filter", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	provisioningFlows: Optional[list[Annotated[Union[IndustryDataAdministrativeUnitProvisioningFlow, IndustryDataClassGroupProvisioningFlow, IndustryDataSecurityGroupProvisioningFlow, IndustryDataUserProvisioningFlow]],Field(discriminator="odata_type")]]] = Field(alias="provisioningFlows", default=None,)

from .industry_data_basic_filter import IndustryDataBasicFilter
from .industry_data_administrative_unit_provisioning_flow import IndustryDataAdministrativeUnitProvisioningFlow
from .industry_data_class_group_provisioning_flow import IndustryDataClassGroupProvisioningFlow
from .industry_data_security_group_provisioning_flow import IndustryDataSecurityGroupProvisioningFlow
from .industry_data_user_provisioning_flow import IndustryDataUserProvisioningFlow

