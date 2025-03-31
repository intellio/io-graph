from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class IndustryDataProvisioningFlowCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[IndustryDataAdministrativeUnitProvisioningFlow, IndustryDataClassGroupProvisioningFlow, IndustryDataSecurityGroupProvisioningFlow, IndustryDataUserProvisioningFlow],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .industry_data_administrative_unit_provisioning_flow import IndustryDataAdministrativeUnitProvisioningFlow
from .industry_data_class_group_provisioning_flow import IndustryDataClassGroupProvisioningFlow
from .industry_data_security_group_provisioning_flow import IndustryDataSecurityGroupProvisioningFlow
from .industry_data_user_provisioning_flow import IndustryDataUserProvisioningFlow
