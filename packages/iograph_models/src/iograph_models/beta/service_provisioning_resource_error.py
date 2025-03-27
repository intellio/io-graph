from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ServiceProvisioningResourceError(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	isResolved: Optional[bool] = Field(alias="isResolved", default=None,)
	serviceInstance: Optional[str] = Field(alias="serviceInstance", default=None,)
	odata_type: Literal["#microsoft.graph.serviceProvisioningResourceError"] = Field(alias="@odata.type", default="#microsoft.graph.serviceProvisioningResourceError")
	errors: Optional[list[Annotated[Union[ServiceProvisioningLinkedResourceErrorDetail],Field(discriminator="odata_type")]]] = Field(alias="errors", default=None,)

from .service_provisioning_linked_resource_error_detail import ServiceProvisioningLinkedResourceErrorDetail

