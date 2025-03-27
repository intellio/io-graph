from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceCompliancePolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AndroidCompliancePolicy, AndroidDeviceOwnerCompliancePolicy, AndroidForWorkCompliancePolicy, AndroidWorkProfileCompliancePolicy, AospDeviceOwnerCompliancePolicy, DefaultDeviceCompliancePolicy, IosCompliancePolicy, MacOSCompliancePolicy, Windows10CompliancePolicy, Windows10MobileCompliancePolicy, Windows81CompliancePolicy, WindowsPhone81CompliancePolicy],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .android_compliance_policy import AndroidCompliancePolicy
from .android_device_owner_compliance_policy import AndroidDeviceOwnerCompliancePolicy
from .android_for_work_compliance_policy import AndroidForWorkCompliancePolicy
from .android_work_profile_compliance_policy import AndroidWorkProfileCompliancePolicy
from .aosp_device_owner_compliance_policy import AospDeviceOwnerCompliancePolicy
from .default_device_compliance_policy import DefaultDeviceCompliancePolicy
from .ios_compliance_policy import IosCompliancePolicy
from .mac_o_s_compliance_policy import MacOSCompliancePolicy
from .windows10_compliance_policy import Windows10CompliancePolicy
from .windows10_mobile_compliance_policy import Windows10MobileCompliancePolicy
from .windows81_compliance_policy import Windows81CompliancePolicy
from .windows_phone81_compliance_policy import WindowsPhone81CompliancePolicy

